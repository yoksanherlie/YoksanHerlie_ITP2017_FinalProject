//script handle

window.onload = () => {
    function scaleContent() {
        let header = $("#main-header"),
            content = $("#main-content");

        content.style = `margin-top: ${header.offsetHeight + 15}px`;
    }

    function initMc() {
        let arr = ['#my-mc-ask-question', '#my-mc-answer-question'];
        let mc = null;
        arr.forEach(a => {
            mc = new McEditor($(a));
            mc.init();
        });
    }

    function initComments() {
        let mc = new McEditor($("#my-mc-editor"));
        mc.init();

        //multiple comments mc editor
        function bindComments() {
            let comments = document.querySelectorAll('.comment-form');
            comments.forEach((el) => {
                let mc = new McEditor(el);
                mc.init();
            });
        }

        bindComments();
    }

    function handleModal() {
        $("#ask-question-button").addEventListener('click', (e) => {
            e.preventDefault();

            $("#ask-question-modal").classList.add('active');
        });

        let answerButton = $("#answer-question-button");
        if (answerButton != null) {
            answerButton.addEventListener("click", (e) => {
                e.preventDefault();

                $("#answer-question-modal").classList.add('active');
            });
        }

        let modals = document.querySelectorAll(".modal-wrapper");
        modals.forEach((el) => {
            el.querySelectorAll(".close, .modal-overlay").forEach((element) => {
                element.addEventListener('click', (e) => {
                    el.classList.remove('active');
                });
            });
        });
        // if (Array.isArray(modals)) {
        // } else {
        //     modals.querySelectorAll(".close, .modal-overlay").forEach((element) => {
        //         element.addEventListener('click', (e) => {
        //             modals.classList.remove('active');
        //         });
        //     });
        // }
    }

    function handleAskQuestion() {
        $("#ask-question").onclick = () => {
            let url = 'http://localhost:8000/quora/ask-question';

            let title = $('#question-title').value,
                question = $("#question-body").innerHTML,
                token = $("input[type='hidden'][name='csrfmiddlewaretoken']").value;

            let formData = new FormData();
            formData.append('title', title);
            formData.append('question', question);
            formData.append('csrfmiddlewaretoken', token);

            let xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);
            xhr.onreadystatechange = () => {
                let data = xhr.responseText;
                location.href = "http://localhost:8000/quora/";
            };
            xhr.send(formData);
        };
    }

    function handleAnswerQuestion() {
        let answer = $("#answer-question");
        if (answer != null) {
            $("#answer-question").onclick = () => {
                let url = 'http://localhost:8000/quora/answer-question';

                let questionId = $('#question-id').value,
                    answer = $("#answer-body").innerHTML,
                    token = $("input[type='hidden'][name='csrfmiddlewaretoken']").value;

                let formData = new FormData();
                formData.append('question_id', questionId);
                formData.append('answer', answer);
                formData.append('csrfmiddlewaretoken', token);

                let xhr = new XMLHttpRequest();
                xhr.open("POST", url, true);
                xhr.onreadystatechange = () => {
                    let data = xhr.responseText;
                    window.location.reload();
                };
                xhr.send(formData);
            };
        }
    }

    function initialize() {
        // own
        handleAskQuestion();
        handleAnswerQuestion();
        
        scaleContent();
        initMc();
        initComments();
        handleModal();
    }

    initialize();
};

window.onload();