class ValueStore {
    constructor() {
        this._resume = null;
        this._grade = null;
        this._school = null;
        this._areaOfInterest = null;
        this._firstName = null;
        this._lastName = null;
        this._linkedinProfileId = null;
    }

    // Getters for the values
    get resume() {
        return this._resume;
    }

    get grade() {
        return this._grade;
    }

    get school() {
        return this._school;
    }

    get areaOfInterest() {
        return this._areaOfInterest;
    }

    get firstName() {
        return this._firstName;
    }

    get lastName() {
        return this._lastName;
    }

    get linkedinProfileId() {
        return this._linkedinProfileId;
    }

    // Setters for the values
    set resume(newResume) {
        this._resume = newResume;
    }

    set grade(newGrade) {
        this._grade = newGrade;
    }

    set school(newSchool) {
        this._school = newSchool;
    }

    set areaOfInterest(newAreaOfInterest) {
        this._areaOfInterest = newAreaOfInterest;
    }

    set firstName(newFirstName) {
        this._firstName = newFirstName;
    }

    set lastName(newLastName) {
        this._lastName = newLastName;
    }

    set linkedinProfileId(newLinkedinProfileId) {
        this._linkedinProfileId = newLinkedinProfileId;
    }
}

const myValueStore = new ValueStore();

// Get references to input elements
const resumeInput = document.getElementById('resume');
const gradeInput = document.getElementById('grade');
const schoolInput = document.getElementById('school');
const areaOfInterestInput = document.getElementById('areaOfInterest');
const firstNameInput = document.getElementById('firstName');
const lastNameInput = document.getElementById('lastName');
const linkedinProfileIdInput = document.getElementById('linkedinProfileId');

// Event listeners to capture user input and store it
resumeInput.addEventListener('input', function() {
    myValueStore.resume = resumeInput.value;
});

gradeInput.addEventListener('input', function() {
    myValueStore.grade = gradeInput.value;
});

schoolInput.addEventListener('input', function() {
    myValueStore.school = schoolInput.value;
});

areaOfInterestInput.addEventListener('input', function() {
    myValueStore.areaOfInterest = areaOfInterestInput.value;
});

firstNameInput.addEventListener('input', function() {
    myValueStore.firstName = firstNameInput.value;
});

lastNameInput.addEventListener('input', function() {
    myValueStore.lastName = lastNameInput.value;
});

linkedinProfileIdInput.addEventListener('input', function() {
    myValueStore.linkedinProfileId = linkedinProfileIdInput.value;
});