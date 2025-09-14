
const stepsList = document.querySelectorAll("#progressBar ul li");
const totalNumberOfSteps = stepsList.length
const stepContainer = document.querySelectorAll(".steps");

/*access button  */
const priviousBtn = document.querySelector("#priviousBtn");
const nextBtn = document.querySelector("#nextBtn");
const submitBtn = document.querySelector("#submitBtn");

/* Change numbrr of step by counting number of li inside progressLine*/
document.documentElement.style.setProperty('--steps',totalNumberOfSteps)


let currentStep = 0

function updateButton(currentStep){
    if(currentStep === 0){
        priviousBtn.style.display="none";
        nextBtn.style.display="block";
        submitBtn.style.display="none";
    }else if(currentStep === (totalNumberOfSteps-1)){
        priviousBtn.style.display="block";
        nextBtn.style.display="none";
        submitBtn.style.display="block";
    }else{
        priviousBtn.style.display="block";
        nextBtn.style.display="block";
        submitBtn.style.display="none";
    }
}

function updateProgress(stepsList,currentStep){
    stepsList.forEach((step, index) =>{
        /*progress line width change according*/
        const progressLine =document.querySelector("#progressLine")
        let progressLinewidth = currentStep / (totalNumberOfSteps - 1);
        console.info(progressLinewidth)
        progressLine.style.transform = `scaleX(${progressLinewidth})`;
  
        // list
        // Each time reset class for recheck again
        step.classList.remove("current","done")
        if (index === currentStep){
            step.classList.add("current")
        }else if(index < currentStep){
            step.classList.add("done")
        }
    })
}

function updateStep(stepContainer, currentStep) {
    stepContainer.forEach((step, index) => {
        // reset first
        step.classList.remove("current");
        step.style.transform = `translateX(-${currentStep * 100}%)`
        // select current
        if (index === currentStep) {
            step.classList.add("current");
        }
    });
}
function validateCurrentStep(stepContainer,currentStep){
    const fieldsInAStep = stepContainer[currentStep].querySelectorAll("input,select");
    for (let field of fieldsInAStep){
        if(!field.reportValidity()){
            return false
        }
    }return true  //check all field then return true
}

/* Privious    */
priviousBtn.addEventListener('click', () =>{
    console.info("priviousBtn Clicked")
    
    if (0 < currentStep){
        currentStep--;
        /* update step*/
    }
    console.info(currentStep);
    updateProgress(stepsList,currentStep);
    updateStep(stepContainer, currentStep);
    updateButton(currentStep);
}
)
/* Next    */
nextBtn.addEventListener('click', () =>{
    console.info("nextBtn Clicked")
    console.info(currentStep)
    if (validateCurrentStep(stepContainer,currentStep)){
        //update step
        if (currentStep < (stepsList.length -1)){
            currentStep++;
        /* update step*/
        }
    
        updateProgress(stepsList,currentStep);
        updateStep(stepContainer, currentStep);
        updateButton(currentStep);
    }
    
}
)
/* Submit    */
submitBtn.addEventListener('click', (e) =>{
   
    console.info("submitBtn Clicked")
}
)