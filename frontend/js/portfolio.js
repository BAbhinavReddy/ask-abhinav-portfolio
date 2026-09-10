const API_BASE_URL =
    "http://127.0.0.1:8000/api";


/* =========================
   API Helper
   ========================= */

async function fetchAPI(endpoint) {

    const response =
        await fetch(
            `${API_BASE_URL}${endpoint}`
        );


    if (!response.ok) {

        throw new Error(
            `Request failed: ${response.status}`
        );

    }


    return response.json();

}


/* =========================
   HTML Safety
   ========================= */

function escapeHTML(value) {

    if (
        value === null ||
        value === undefined
    ) {

        return "";

    }


    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");

}


/* =========================
   Profile
   ========================= */

async function loadProfile() {

    try {

        const profile =
            await fetchAPI("/profile");


        /*
         * Store the email globally so
         * the email popup can use the
         * database value.
         */

        portfolioEmail =
            profile.email;


        const heroName =
            document.getElementById(
                "hero-name"
            );


        const heroTitle =
            document.getElementById(
                "hero-title"
            );


        const heroSummary =
            document.getElementById(
                "hero-summary"
            );


        const aboutSummary =
            document.getElementById(
                "about-summary"
            );


        if (heroName) {

            heroName.textContent =
                profile.name;

        }


        if (heroTitle) {

            heroTitle.textContent =
                profile.title;

        }


        if (heroSummary) {

            heroSummary.textContent =
                profile.summary;

        }


        if (aboutSummary) {

            aboutSummary.textContent =
                profile.summary;

        }


        /* =========================
           Contact Links
           ========================= */

        const phoneLink =
            document.getElementById(
                "phone-link"
            );


        const githubLink =
            document.getElementById(
                "github-link"
            );


        const linkedinLink =
            document.getElementById(
                "linkedin-link"
            );


        if (phoneLink) {

            phoneLink.dataset.phone =
                profile.phone;

        }


        if (githubLink) {

            githubLink.href =
                profile.github;

        }


        if (linkedinLink) {

            linkedinLink.href =
                profile.linkedin;

        }


    } catch (error) {

        console.error(
            "Failed to load profile:",
            error
        );

    }

}


/* =========================
   Skills
   ========================= */

async function loadSkills() {

    try {

        const skills =
            await fetchAPI("/skills");


        const container =
            document.getElementById(
                "skills-container"
            );


        if (!container) {

            return;

        }


        container.innerHTML = "";


        /*
         * Group database skills
         * by category.
         */

        const groupedSkills = {};


        skills.forEach(
            (skill) => {

                const category =
                    skill.category ||
                    "Other";


                if (
                    !groupedSkills[category]
                ) {

                    groupedSkills[category] =
                        [];

                }


                groupedSkills[category].push(
                    skill
                );

            }
        );


        Object.entries(
            groupedSkills
        ).forEach(
            ([category, categorySkills]) => {

                const card =
                    document.createElement(
                        "article"
                    );


                card.className =
                    "skill-card";


                const categoryTitle =
                    document.createElement(
                        "div"
                    );


                categoryTitle.className =
                    "skill-category";


                categoryTitle.textContent =
                    category;


                const skillsList =
                    document.createElement(
                        "div"
                    );


                skillsList.className =
                    "skill-list";


                categorySkills.forEach(
                    (skill) => {

                        const skillTag =
                            document.createElement(
                                "span"
                            );


                        skillTag.className =
                            "skill-tag";


                        skillTag.textContent =
                            skill.name;


                        skillsList.appendChild(
                            skillTag
                        );

                    }
                );


                card.appendChild(
                    categoryTitle
                );


                card.appendChild(
                    skillsList
                );


                container.appendChild(
                    card
                );

            }
        );


    } catch (error) {

        console.error(
            "Failed to load skills:",
            error
        );

    }

}


/* =========================
   Experience
   ========================= */

async function loadExperience() {

    try {

        const experiences =
            await fetchAPI(
                "/experience"
            );


        const container =
            document.getElementById(
                "experience-container"
            );


        if (!container) {

            return;

        }


        container.innerHTML = "";


        experiences.forEach(
            (experience) => {

                const item =
                    document.createElement(
                        "article"
                    );


                item.className =
                    "experience-item";


                const startDate =
                    formatDate(
                        experience.start_date
                    );


                const endDate =
                    experience.end_date
                        ? formatDate(
                            experience.end_date
                        )
                        : "Present";


                item.innerHTML = `

                    <div class="experience-header">

                        <div>

                            <div class="experience-role">
                                ${escapeHTML(
                                    experience.role
                                )}
                            </div>

                            <div class="experience-company">
                                ${escapeHTML(
                                    experience.company
                                )}
                            </div>

                        </div>


                        <div class="experience-date">
                            ${escapeHTML(startDate)}
                            –
                            ${escapeHTML(endDate)}
                        </div>

                    </div>


                    <div class="experience-location">
                        ${escapeHTML(
                            experience.location
                        )}
                    </div>


                    <p class="experience-description">
                        ${escapeHTML(
                            experience.description
                        )}
                    </p>

                `;


                container.appendChild(
                    item
                );

            }
        );


    } catch (error) {

        console.error(
            "Failed to load experience:",
            error
        );

    }

}


/* =========================
   Projects
   ========================= */

async function loadProjects() {

    try {

        const projects =
            await fetchAPI(
                "/projects"
            );


        const container =
            document.getElementById(
                "projects-container"
            );


        if (!container) {

            return;

        }


        container.innerHTML = "";


        projects.forEach(
            (project) => {

                const card =
                    document.createElement(
                        "article"
                    );


                card.className =
                    "project-card";


                const githubLink =
                    project.github_url
                        ? `
                            <a
                                class="project-link"
                                href="${escapeHTML(
                                    project.github_url
                                )}"
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                View on GitHub →
                            </a>
                        `
                        : "";


                card.innerHTML = `

                    <h3>
                        ${escapeHTML(
                            project.name
                        )}
                    </h3>


                    <p>
                        ${escapeHTML(
                            project.description
                        )}
                    </p>


                    ${githubLink}

                `;


                container.appendChild(
                    card
                );

            }
        );


    } catch (error) {

        console.error(
            "Failed to load projects:",
            error
        );

    }

}


/* =========================
   Education Logo
   ========================= */

function getEducationLogo(
    institution
) {

    const normalizedInstitution =
        institution.toLowerCase();


    if (
        normalizedInstitution.includes(
            "missouri-kansas"
        ) ||
        normalizedInstitution.includes(
            "university of missouri"
        )
    ) {

        return "assets/images/umkc-logo.png";

    }


    if (
        normalizedInstitution.includes(
            "vidya jyothi"
        )
    ) {

        return "assets/images/vjit-logo.png";

    }


    return null;

}


/* =========================
   Education
   ========================= */

async function loadEducation() {

    try {

        const education =
            await fetchAPI(
                "/education"
            );


        const container =
            document.getElementById(
                "education-container"
            );


        if (!container) {

            return;

        }


        container.innerHTML = "";


        education.forEach(
            (item) => {

                const element =
                    document.createElement(
                        "article"
                    );


                element.className =
                    "education-item";


                const logo =
                    getEducationLogo(
                        item.institution
                    );


                const logoHTML =
                    logo
                        ? `
                            <div class="education-logo">

                                <img
                                    src="${logo}"
                                    alt="${escapeHTML(
                                        item.institution
                                    )} logo"
                                >

                            </div>
                        `
                        : "";


                const endYear =
                    item.end_year ??
                    "Present";


                const gpaHTML =
                    item.gpa !== null &&
                    item.gpa !== undefined
                        ? `
                            <span>
                                GPA:
                                ${escapeHTML(
                                    item.gpa
                                )}
                            </span>
                        `
                        : "";


                element.innerHTML = `

                    ${logoHTML}


                    <div class="education-details">

                        <div class="education-institution">
                            ${escapeHTML(
                                item.institution
                            )}
                        </div>


                        <div class="education-degree">
                            ${escapeHTML(
                                item.degree
                            )}
                            —
                            ${escapeHTML(
                                item.field_of_study
                            )}
                        </div>


                        <div class="education-years">

                            <span>
                                ${escapeHTML(
                                    item.start_year
                                )}
                                –
                                ${escapeHTML(
                                    endYear
                                )}
                            </span>


                            ${gpaHTML}

                        </div>

                    </div>

                `;


                container.appendChild(
                    element
                );

            }
        );


    } catch (error) {

        console.error(
            "Failed to load education:",
            error
        );

    }

}


/* =========================
   Date Formatting
   ========================= */

function formatDate(
    dateString
) {

    if (!dateString) {

        return "";

    }


    const date =
        new Date(dateString);


    if (
        Number.isNaN(
            date.getTime()
        )
    ) {

        return dateString;

    }


    return date.toLocaleDateString(
        "en-US",
        {
            month: "short",
            year: "numeric",
        }
    );

}


/* =========================
   Initialize Portfolio
   ========================= */

document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadProfile();

        loadSkills();

        loadExperience();

        loadProjects();

        loadEducation();

    }
);