class McEditor {
    constructor(target) {
        this.target = target;
    }

    check() {
        if (typeof this.body === 'undefined') return false;

        return true;
    }

    preset() {
        this.body.contentEditable = "true";
    }

    applyCommand(command) {
        if (command === 'createlink') {
            let url = prompt('Enter the link here: ','http:\/\/');
            if (url) {
                document.execCommand(command, false, url);
            }
            this.body.focus();
        } else {
            this.body.focus();
            console.log(command);
            document.execCommand(command, false, null);
        }
    }

    handle() {
        this.body.addEventListener('dragover', (e) => {
            e.preventDefault();
            return false;
        });

        this.body.addEventListener('drop', (e) => {
            e.preventDefault();
            return false;
        });

        // this.target.querySelectorAll(".mc-editor-nav li").forEach((item) => {
        //     item.querySelector('a').addEventListener('click', (e) => {
        //         let _this = item.querySelector('a'),
        //             command = _this.getAttribute('data-command');

        //         this.applyCommand(command);
        //     });
        // });
    }

    init() {
        if (!this.target) return;
        this.body = this.target.querySelectorAll('.mc-editor-body')[0];

        if (!this.check()) {
            throw 'Something wrong with McEditor.';
        } else {
            this.preset();
            this.handle();
        }
    }
}