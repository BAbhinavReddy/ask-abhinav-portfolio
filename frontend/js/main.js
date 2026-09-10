/* =========================
   Portfolio Email
   ========================= */

let portfolioEmail = "";


/* =========================
   Navigation
   ========================= */

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const navLinks =
            document.querySelectorAll(
                ".navbar nav a"
            );


        const sections =
            document.querySelectorAll(
                "main section[id]"
            );


        /* =========================
           Active Navigation
           ========================= */

        const updateActiveNavigation =
            () => {

                let currentSection =
                    "home";


                const scrollPosition =
                    window.scrollY + 150;


                sections.forEach(
                    (section) => {

                        const sectionTop =
                            section.offsetTop;


                        const sectionBottom =
                            sectionTop +
                            section.offsetHeight;


                        if (
                            scrollPosition >=
                                sectionTop &&
                            scrollPosition <
                                sectionBottom
                        ) {

                            currentSection =
                                section.id;

                        }

                    }
                );


                navLinks.forEach(
                    (link) => {

                        link.classList.remove(
                            "active"
                        );


                        const href =
                            link.getAttribute(
                                "href"
                            );


                        if (
                            href ===
                            `#${currentSection}`
                        ) {

                            link.classList.add(
                                "active"
                            );

                        }

                    }
                );

            };


        window.addEventListener(
            "scroll",
            updateActiveNavigation,
            {
                passive: true,
            }
        );


        updateActiveNavigation();


        /* =========================
           Smooth Navigation
           ========================= */

        navLinks.forEach(
            (link) => {

                link.addEventListener(
                    "click",
                    (event) => {

                        const targetId =
                            link.getAttribute(
                                "href"
                            );


                        if (
                            !targetId ||
                            !targetId.startsWith("#")
                        ) {

                            return;

                        }


                        const target =
                            document.querySelector(
                                targetId
                            );


                        if (!target) {

                            return;

                        }


                        event.preventDefault();


                        target.scrollIntoView({
                            behavior: "smooth",
                            block: "start",
                        });

                    }
                );

            }
        );

    }
);


/* =========================
   Email Popup
   ========================= */

function initializeEmailPopup() {

    const emailButton =
        document.getElementById(
            "email-link"
        );


    const emailModal =
        document.getElementById(
            "email-modal"
        );


    const emailModalClose =
        document.getElementById(
            "email-modal-close"
        );


    const emailDisplay =
        document.getElementById(
            "email-display"
        );


    const copyEmailButton =
        document.getElementById(
            "copy-email-button"
        );


    const copyEmailStatus =
        document.getElementById(
            "copy-email-status"
        );


    if (
        !emailButton ||
        !emailModal
    ) {

        return;

    }


    /* =========================
       Open
       ========================= */

    emailButton.addEventListener(
        "click",
        () => {

            emailDisplay.textContent =
                portfolioEmail ||
                "Email unavailable";


            emailModal.classList.remove(
                "hidden"
            );


            emailModal.setAttribute(
                "aria-hidden",
                "false"
            );

        }
    );


    /* =========================
       Close
       ========================= */

    emailModalClose.addEventListener(
        "click",
        closeEmailModal
    );


    /* =========================
       Outside Click
       ========================= */

    emailModal.addEventListener(
        "click",
        (event) => {

            if (
                event.target ===
                emailModal
            ) {

                closeEmailModal();

            }

        }
    );


    /* =========================
       Copy
       ========================= */

    copyEmailButton.addEventListener(
        "click",
        async () => {

            if (!portfolioEmail) {

                return;

            }


            try {

                await navigator.clipboard.writeText(
                    portfolioEmail
                );


                copyEmailStatus.textContent =
                    "✓ Email copied!";


                copyEmailButton.textContent =
                    "Copied!";


                setTimeout(
                    () => {

                        copyEmailStatus.textContent =
                            "";

                        copyEmailButton.textContent =
                            "Copy";

                    },
                    2000
                );


            } catch (error) {

                console.error(
                    "Failed to copy email:",
                    error
                );


                copyEmailStatus.textContent =
                    "Unable to copy automatically.";

            }

        }
    );


    /* =========================
       Escape Key
       ========================= */

    document.addEventListener(
        "keydown",
        (event) => {

            if (
                event.key === "Escape"
            ) {

                closeEmailModal();

            }

        }
    );

}


function closeEmailModal() {

    const emailModal =
        document.getElementById(
            "email-modal"
        );


    if (!emailModal) {

        return;

    }


    emailModal.classList.add(
        "hidden"
    );


    emailModal.setAttribute(
        "aria-hidden",
        "true"
    );

}

function initializePhonePopup() {
    const phoneButton = document.getElementById("phone-link");
    const phoneModal = document.getElementById("phone-modal");
    const phoneModalClose = document.getElementById("phone-modal-close");
    const phoneDisplay = document.getElementById("phone-display");
    const copyPhoneButton = document.getElementById("copy-phone-button");
    const copyPhoneStatus = document.getElementById("copy-phone-status");

    if (!phoneButton || !phoneModal) return;

    phoneButton.addEventListener("click", () => {
        const phoneLink = document.getElementById("phone-link");

        const phoneNumber =
            phoneLink?.dataset.phone || "Phone unavailable";

        phoneDisplay.textContent = phoneNumber;

        phoneModal.classList.remove("hidden");
        phoneModal.setAttribute("aria-hidden", "false");
    });

    phoneModalClose.addEventListener("click", closePhoneModal);

    phoneModal.addEventListener("click", (event) => {
        if (event.target === phoneModal) {
            closePhoneModal();
        }
    });

    copyPhoneButton.addEventListener("click", async () => {
        const phoneNumber = phoneDisplay.textContent;

        if (!phoneNumber || phoneNumber === "Phone unavailable") {
            return;
        }

        try {
            await navigator.clipboard.writeText(phoneNumber);

            copyPhoneStatus.textContent = "✓ Phone number copied!";
            copyPhoneButton.textContent = "Copied!";

            setTimeout(() => {
                copyPhoneStatus.textContent = "";
                copyPhoneButton.textContent = "Copy";
            }, 2000);
        } catch (error) {
            console.error("Failed to copy phone number:", error);
            copyPhoneStatus.textContent =
                "Unable to copy automatically.";
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closePhoneModal();
        }
    });
}

function closePhoneModal() {
    const phoneModal = document.getElementById("phone-modal");

    if (!phoneModal) return;

    phoneModal.classList.add("hidden");
    phoneModal.setAttribute("aria-hidden", "true");
}

document.addEventListener("DOMContentLoaded", initializePhonePopup);


document.addEventListener(
    "DOMContentLoaded",
    initializeEmailPopup
);