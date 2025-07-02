document.addEventListener("DOMContentLoaded", function () {
    const correctAnswers = {
    q1: "q1a2",
    q2: "q2a2",
    q3: "q3a3",
    q4: "q4a3",
    q5: "q5a2",
    q6: "q6a3",
    };

    Object.keys(correctAnswers).forEach((q) => {
    const buttons = document.querySelectorAll(`[id^=${q}]`);
    const feedback = document.getElementById("feedback" + q.slice(-1));

    buttons.forEach((btn) => {
        btn.addEventListener("click", () => {
        buttons.forEach((b) => {
            b.disabled = true;
            b.classList.remove("correct", "incorrect");
        });

        if (btn.id === correctAnswers[q]) {
            btn.classList.add("correct");
            feedback.textContent = "Correct!";
        } else {
            btn.classList.add("incorrect");
            feedback.textContent = "Incorrect";
        }
        });
    });
    });

    // Model Answer Buttons
    for (let i = 1; i <= 2; i++) {
    const btn = document.getElementById(`showAnswerBtn${i}`);
    const answer = document.getElementById(`modelAnswer${i}`);
    btn.addEventListener("click", () => {
        const isVisible = answer.style.display === "block";
        answer.style.display = isVisible ? "none" : "block";
        btn.textContent = isVisible ? "Show Model Answer" : "Hide Model Answer";
    });
    }
});
