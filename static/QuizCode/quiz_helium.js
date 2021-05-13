// Elements to the information before begining the Quiz
//const info1 = document.getElementById('id');
//const info3 = document.getElementById('id2');
//const info2 = document.getElementById('id1');
const info4 = document.getElementById("id3");
const info5 = document.getElementById("id4");
const info6 = document.getElementById("id5");

//the button to start the quiz 
const startbutton = document.getElementById("start")

// The Quiz element
var quiz = document.getElementById("quiz");

function startQuiz(){
    //Hiding the infomation elements
    info4.remove();
    info5.remove();
    info6.remove();

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
        question: "When do scientist believe helium was created?",
        choiceA : "Ten years ago.",
        choiceB : "1800",
        choiceC : "The begining of the unverise.",
        correct : "C"
    },{
        question : "Which of the following does helium help float??",
        choiceA : "Cars and Motorcycles",
        choiceB : "Airoplanes and Submerines",
        choiceC : "Balloons and Airships ",
        correct : "C"
    },
    {
        question : "Helium consists of __ protons and __ electrons. fill in the blanks.",
        choiceA : "2 & 2",
        choiceB : "4 & 4",
        choiceC : "3 & 10",
        correct : "A"     
    }
];

//present the questions for the quiz
//Elements
const question = document.getElementById('question');
const choiceA = document.getElementById('A');
const choiceB = document.getElementById('B');
const choiceC = document.getElementById('C');
const score = document.getElementById("score");

//Creating varaible to assist changing questions
let currentQuestion = 0;
let grade = 0;


//Function to display the quiz
function displayQuestion(){ 
    let q = quizQuestions[currentQuestion];
    question.innerHTML = "Question " + (currentQuestion + 1) + ": " + q.question;
    choiceA.innerHTML = q.choiceA;
    choiceB.innerHTML = q.choiceB;
    choiceC.innerHTML = q.choiceC;
}

//Checking the Answers and moving onto the next question
function checkAnswer(answer){
    if(answer==quizQuestions[currentQuestion].correct){
        grade++;
    }
    if(currentQuestion < (quizQuestions.length -1)){
        currentQuestion++;
        displayQuestion();
    }
    else{
        displayResults();
    }
}

//Displaying the results
//elements
const endQuizContent = document.getElementById("endQuizContent");
const displayGrade = document.getElementById("displayGrade");
const quizDiv = document.getElementById("quizDiv");

//Resultsed displayed 
//Still need to round the results to 2 decimal places
function displayResults(){
    quizDiv.remove();
    quiz.style.display = "none";
    endQuizContent.style = 'display';
    displayGrade.innerHTML = "Your Grade was " + ((grade/quizQuestions.length)*100).toFixed() + "%";
}