const chatButton = document.getElementById("chat-button");
const chatWindow = document.getElementById("chat-window");
const chatClose = document.getElementById("chat-close");
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");
const chatMessages = document.getElementById("chat-messages");

const ASK_API_URL = "http://127.0.0.1:8000/api/ask";


/* =========================
   Add Chat Message
   ========================= */

function addMessage(text, sender) {
    const message = document.createElement("div");

    message.className = `chat-message ${sender}`;
    message.textContent = text;

    chatMessages.appendChild(message);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}


/* =========================
   Loading State
   ========================= */

function setLoading(isLoading) {
    chatInput.disabled = isLoading;

    const submitButton = chatForm.querySelector(
        "button[type='submit']"
    );

    if (submitButton) {
        submitButton.disabled = isLoading;
    }
}


/* =========================
   Open Chat
   ========================= */

chatButton.addEventListener("click", () => {
    chatWindow.classList.remove("hidden");

    chatInput.focus();
});


/* =========================
   Close Chat
   ========================= */

chatClose.addEventListener("click", () => {
    chatWindow.classList.add("hidden");
});


/* =========================
   Submit Question
   ========================= */

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const question = chatInput.value.trim();

    if (!question) {
        return;
    }

    // Show user's question
    addMessage(question, "user");

    // Clear input
    chatInput.value = "";

    // Disable input while waiting
    setLoading(true);

    // Show temporary loading message
    addMessage("Thinking...", "assistant");

    try {
        const response = await fetch(ASK_API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                question: question,
            }),
        });

        if (!response.ok) {
            throw new Error(
                `Request failed: ${response.status}`
            );
        }

        const data = await response.json();

        /*
         * Find the most recent assistant message.
         * This should be the "Thinking..." message.
         */
        const assistantMessages =
            chatMessages.querySelectorAll(
                ".chat-message.assistant"
            );

        const loadingMessage =
            assistantMessages[assistantMessages.length - 1];

        if (
            loadingMessage &&
            loadingMessage.textContent === "Thinking..."
        ) {
            loadingMessage.textContent = data.answer;
        } else {
            addMessage(data.answer, "assistant");
        }

    } catch (error) {
        console.error(
            "Ask Abhinav request failed:",
            error
        );

        const assistantMessages =
            chatMessages.querySelectorAll(
                ".chat-message.assistant"
            );

        const loadingMessage =
            assistantMessages[assistantMessages.length - 1];

        if (
            loadingMessage &&
            loadingMessage.textContent === "Thinking..."
        ) {
            loadingMessage.textContent =
                "Sorry, I couldn't answer that right now.";
        }

    } finally {
        setLoading(false);
        chatInput.focus();
    }
});