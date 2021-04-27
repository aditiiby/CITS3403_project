const startbutton = document.getElementById('start')
var factsTitle = document.getElementById('id');
var factsList = document.getElementById('id1');
var clickWhenReady = document.getElementById('id2');
var table = document.getElementById("id3");
var quiz = document.getElementById("quiz");

function startQuiz(){
    factsTitle.remove();
    factsList.remove();
    clickWhenReady.remove();
    table.remove();
    start.style.display = "none";
    quiz.style = "display";
    displayQuestion();
}

let options = [
    {
        question: "What is the lightest elemnt on earth?",
        choiceA : "Hydrogen",
        choiceB : "Helium",
        choiceC : "Oxygen",
        correct : "Hydrogen"
    },{
        question : "What combines with hydrogen to create water?",
        choiceA : "Helium",
        choiceB : "Oxygen",
        choiceC : "Air",
        correct : "B"
    }
];

const question = document.getElementById('question');
const choiceA = document.getElementById('A');
const choiceB = document.getElementById('B');
const choiceC = document.getElementById('C');
const score = document.getElementById("score");

// question counter 
let x = 0;

function displayQuestion(){ 
    questionNum.innerHTML = "Question";
    question.innerHTML = options[x].question;
    choiceA.innerHTML = options[x].choiceA;
    choiceB.innerHTML = options[x].choiceB;
    choiceC.innerHTML = options[x].choiceC;
}

// score counter
let grade = 0;

// Checking the To see if the answer is correct.
function checkAnswerA(){
    if(options[0].choiceA == options[0].correct){
        grade = grade +1
        score.innerHTML = grade;
    }
    else{
        score.innerHTML = grade
    }
}

function checkAnswerB(){
    if(options[0].choiceB == options[0].correct){
        grade = grade +1
        score.innerHTML = grade;
    }
    else{
        score.innerHTML = grade
    }
}
function checkAnswerC(){
    if(options[0].choiceC == options[0].correct){
        grade = grade + 1
        score.innerHTML = grade;
    }
    else{
        score.innerHTML = grade
    }
}

