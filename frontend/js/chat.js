/* =========================
   Chat Elements
   ========================= */

const chatButton =
    document.getElementById(
        "chat-button"
    );


const chatWindow =
    document.getElementById(
        "chat-window"
    );


const chatClose =
    document.getElementById(
        "chat-close"
    );


const chatForm =
    document.getElementById(
        "chat-form"
    );


const chatInput =
    document.getElementById(
        "chat-input"
    );


const chatMessages =
    document.getElementById(
        "chat-messages"
    );


const ASK_API_URL =
    "http://127.0.0.1:8000/api/ask";


/* =========================
   Add Message
   ========================= */

function addMessage(text, sender) {
    const message = document.createElement("div");
    message.className = `chat-message ${sender}`;

    if (sender === "assistant") {
        message.innerHTML = renderMarkdown(text);
    } else {
        message.textContent = text;
    }

    chatMessages.appendChild(message);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    return message;
}

function renderMarkdown(text) {
    const escaped = escapeHTML(text);

    return escaped
        // Bold: **text**
        .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")

        // Italic: *text*
        .replace(/(?<!\*)\*([^*]+?)\*(?!\*)/g, "<em>$1</em>")

        // Inline code: `text`
        .replace(/`([^`]+)`/g, "<code>$1</code>")

        // Line breaks
        .replace(/\n/g, "<br>");
}

function escapeHTML(value) {
    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}


/* =========================
   Loading State
   ========================= */

function setLoading(
    isLoading
) {

    if (chatInput) {

        chatInput.disabled =
            isLoading;

    }


    const submitButton =
        chatForm?.querySelector(
            "button[type='submit']"
        );


    if (submitButton) {

        submitButton.disabled =
            isLoading;

    }

}


/* =========================
   Open Chat
   ========================= */

function openChat() {

    if (!chatWindow) {

        return;

    }


    chatWindow.classList.remove(
        "hidden"
    );


    if (chatInput) {

        setTimeout(
            () => {

                chatInput.focus();

            },
            100
        );

    }

}


if (chatButton) {

    chatButton.addEventListener(
        "click",
        openChat
    );

}


/* =========================
   Close Chat
   ========================= */

function closeChat() {

    if (!chatWindow) {

        return;

    }


    chatWindow.classList.add(
        "hidden"
    );

}


if (chatClose) {

    chatClose.addEventListener(
        "click",
        closeChat
    );

}


/* =========================
   Escape Key
   ========================= */

document.addEventListener(
    "keydown",
    (event) => {

        if (
            event.key === "Escape" &&
            chatWindow &&
            !chatWindow.classList.contains(
                "hidden"
            )
        ) {

            closeChat();

        }

    }
);


/* =========================
   Submit Question
   ========================= */

if (chatForm) {

    chatForm.addEventListener(
        "submit",
        async (event) => {

            event.preventDefault();


            const question =
                chatInput.value.trim();


            if (!question) {

                return;

            }


            /* =========================
               User Message
               ========================= */

            addMessage(
                question,
                "user"
            );


            chatInput.value = "";


            /* =========================
               Loading
               ========================= */

            setLoading(true);


            const loadingMessage =
                addMessage(
                    "Thinking...",
                    "assistant"
                );


            try {

                const response =
                    await fetch(
                        ASK_API_URL,
                        {
                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json",
                            },

                            body: JSON.stringify({
                                question:
                                    question,
                            }),

                        }
                    );


                if (!response.ok) {

                    throw new Error(
                        `Request failed: ${response.status}`
                    );

                }


                const data =
                    await response.json();


                if (
                    loadingMessage &&
                    data.answer
                ) {

                    loadingMessage.innerHTML =
                        renderMarkdown(data.answer);

                } else {

                    addMessage(
                        data.answer ||
                        "I couldn't generate an answer.",
                        "assistant"
                    );

                }


            } catch (error) {

                console.error(
                    "Ask Abhinav request failed:",
                    error
                );


                if (loadingMessage) {

                    loadingMessage.textContent =
                        "Sorry, I couldn't answer that right now.";

                } else {

                    addMessage(
                        "Sorry, I couldn't answer that right now.",
                        "assistant"
                    );

                }


            } finally {

                setLoading(false);


                if (chatInput) {

                    chatInput.focus();

                }

            }

        }
    );

}