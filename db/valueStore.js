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

}