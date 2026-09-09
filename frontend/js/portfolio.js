const API_BASE_URL = "http://127.0.0.1:8000/api";


async function fetchAPI(endpoint) {
    const response = await fetch(
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
   Profile
   ========================= */

async function loadProfile() {
    try {
        const profile = await fetchAPI("/profile");

        document.getElementById("hero-name").textContent =
            profile.name;

        document.getElementById("hero-title").textContent =
            profile.title;

        document.getElementById("hero-summary").textContent =
            profile.summary;

        document.getElementById("about-summary").textContent =
            profile.summary;

        document.getElementById("email-link").href =
            `mailto:${profile.email}`;

        document.getElementById("phone-link").href =
            `tel:${profile.phone}`;

        document.getElementById("github-link").href =
            profile.github;

        document.getElementById("linkedin-link").href =
            profile.linkedin;

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
        const skills = await fetchAPI("/skills");

        const container =
            document.getElementById("skills-container");

        container.innerHTML = "";

        skills.forEach((skill) => {
            const card = document.createElement("div");

            card.className = "skill-card";

            card.textContent = skill.name;

            container.appendChild(card);
        });

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
            await fetchAPI("/experience");

        const container =
            document.getElementById("experience-container");

        container.innerHTML = "";

        experiences.forEach((experience) => {
            const item =
                document.createElement("article");

            item.className = "experience-item";

            const startDate =
                formatDate(experience.start_date);

            const endDate =
                experience.end_date
                    ? formatDate(experience.end_date)
                    : "Present";

            item.innerHTML = `
                <div class="experience-header">
                    <div>
                        <div class="experience-role">
                            ${experience.role}
                        </div>

                        <div class="experience-company">
                            ${experience.company}
                        </div>
                    </div>

                    <div class="experience-date">
                        ${startDate} – ${endDate}
                    </div>
                </div>

                <div class="experience-location">
                    ${experience.location}
                </div>

                <p class="experience-description">
                    ${experience.description}
                </p>
            `;

            container.appendChild(item);
        });

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
            await fetchAPI("/projects");

        const container =
            document.getElementById("projects-container");

        container.innerHTML = "";

        projects.forEach((project) => {
            const card =
                document.createElement("article");

            card.className = "project-card";

            const githubLink =
                project.github_url
                    ? `
                        <a
                            class="project-link"
                            href="${project.github_url}"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            View on GitHub →
                        </a>
                    `
                    : "";

            card.innerHTML = `
                <h3>
                    ${project.name}
                </h3>

                <p>
                    ${project.description}
                </p>

                ${githubLink}
            `;

            container.appendChild(card);
        });

    } catch (error) {
        console.error(
            "Failed to load projects:",
            error
        );
    }
}


/* =========================
   Education
   ========================= */

async function loadEducation() {
    try {
        const education =
            await fetchAPI("/education");

        const container =
            document.getElementById("education-container");

        container.innerHTML = "";

        education.forEach((item) => {
            const element =
                document.createElement("article");

            element.className = "education-item";

            element.innerHTML = `
                <div class="education-institution">
                    ${item.institution}
                </div>

                <div class="education-degree">
                    ${item.degree}
                    — ${item.field_of_study}
                </div>

                <div class="education-years">
                    ${item.start_year} – ${item.end_year ?? "Present"}
                </div>
            `;

            container.appendChild(element);
        });

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

function formatDate(dateString) {
    const date = new Date(dateString);

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