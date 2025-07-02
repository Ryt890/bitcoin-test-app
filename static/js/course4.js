document.addEventListener("DOMContentLoaded", function () {
    // 正解のマッピング
    const correctAnswers = {
        q1: "q1a1",
        q2: "q2a3",
        q3: "q3a2",
    };

    // 4択問題のセットアップ
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

    // 自由記述の模範解答表示ボタン
    const showAnswerBtn = document.getElementById("showAnswerBtn");
    const modelAnswer = document.getElementById("modelAnswer");

    showAnswerBtn.addEventListener("click", () => {
        if (modelAnswer.style.display === "none") {
            modelAnswer.style.display = "block";
            showAnswerBtn.textContent = "Hide Model Answer";
        } else {
            modelAnswer.style.display = "none";
            showAnswerBtn.textContent = "Show Model Answer";
        }
    });
});
