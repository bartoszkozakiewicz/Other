window.onload = function (){
    console.log("app started");
    calculator.init();
};

let calculator = {
    buttons: undefined,
    input: undefined,

    init: function (){
        this.buttons = document.querySelectorAll(".numbers button, .operators button");//Pozwala wyłapywać elementy tak jak w kodzie css
        //console.log(this.buttons);
        this.input = document.getElementById("input");

        for(let i = 0; i < this.buttons.length; i++)
        {
            let el = this.buttons[i];
            el.addEventListener("click", this.buttonClick);//Drugie to nazwa funkcji, ktora bedzie wywołana kiedy uzytkownik kliknie na button, co mowi pierwszy element "click"
        }
    },
    buttonClick: function (e){
        let divHtmlText = e.target.innerHTML; // target to ten przycisk, ktory nacisnelismy
        console.log("Klik: " + divHtmlText);
        switch(divHtmlText){
            case "=":
                calculator.evaluate();
            break;
            case "1":
            case "2":
            case "3":
            case "4":
            case "5":
            case "6":
            case "7":
            case "8":
            case "9":
            case "0":
            case "00":
            case ".":
            case "+":
            case "-":
            case "*":
            case "/":
                calculator.addToInput(divHtmlText);
            break;
            case "C":
                calculator.input.value = "";
            break;     
        }
    },
    addToInput: function(str){
        this.input.value += str;
    },
    evaluate: function(){
        let result = math.evaluate(calculator.input.value);
        calculator.input.value = result;
    }
};