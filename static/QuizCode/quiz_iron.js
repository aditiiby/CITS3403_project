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

function startQuiz() {
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
let quizQuestions = [{
        question: "Iron consists of __ protons and __ electrons. Fill in the blanks.",
        choiceA: "26 & 26",
        choiceB: "1 & 1",
        choiceC: "3 & 3",
        correct: "A"
    }, {
        question: "What is the most abundant element in th earth?",
        choiceA: "Helium",
        choiceB: "Iron",
        choiceC: "Air",
        correct: "B"
    },
    {
        question: "What is the melting point of iron in degree celsius? ",
        choiceA: "1538",
        choiceB: "23",
        choiceC: "2800",
        correct: "A"
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
function displayQuestion() {
    let q = quizQuestions[currentQuestion];
    question.innerHTML = "Question " + (currentQuestion + 1) + ": " + q.question;
    choiceA.innerHTML = q.choiceA;
    choiceB.innerHTML = q.choiceB;
    choiceC.innerHTML = q.choiceC;
}

//Checking the Answers and moving onto the next question
function checkAnswer(answer) {
    if (answer == quizQuestions[currentQuestion].correct) {
        grade++;
    }
    if (currentQuestion < (quizQuestions.length - 1)) {
        currentQuestion++;
        displayQuestion();
    } else {
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
function displayResults() {
    quizDiv.remove();
    quiz.style.display = "none";
    endQuizContent.style = 'display';
    displayGrade.innerHTML = "Your Grade was " + ((grade / quizQuestions.length) * 100).toFixed() + "%";
    $.ajax({
        type: 'POST',
        url: '/iron',
        data: JSON.stringify(((grade / quizQuestions.length) * 100).toFixed()),
        contentType: 'application/json'
    });
}