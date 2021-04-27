// Elements to the information before begining the Quiz
const info1 = document.getElementById('id');
const info2 = document.getElementById('id1');
const info3 = document.getElementById('id2');
const info4 = document.getElementById("id3");

//the button to start the quiz 
const startbutton = document.getElementById("start")

// The Quiz element
var quiz = document.getElementById("quiz");

function startQuiz(){
    //Hiding the infomation elements
    info1.remove();
    info2.remove();
    info3.remove();
    info4.remove();

    //Hide the button
    startbutton.style.display = "none";
    //Displaying the Quiz
    quiz.style = "display";
    //Display the Quiz
    displayQuestion();
}

// The questions, multi choice answers and the answer for the quiz
let quizQuestions = [
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

//present the questions for the quiz
//Elements
const question = document.getElementById('question');
const choiceA = document.getElementById('A');
const choiceB = document.getElementById('B');
const choiceC = document.getElementById('C');

function displayQuestion(){ 
    let q = quizQuestions[0];
    question.innerHTML = "Question :" + q.question;
    choiceA.innerHTML = q.choiceA;
    choiceB.innerHTML = q.choiceB;
    choiceC.innerHTML = q.choiceC;
}