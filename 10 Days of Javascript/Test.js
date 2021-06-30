// Test: Notes Store
var completedNotes = [];
var activeNotes = [];
var otherNotes = [];

class NotesStore {

    addNote(state, name) {
        if (name === '') {
            throw new Error('Name cannot be empty');
        }
        if (!this.isValid(state)) {
            throw new Error('Invalid state ' + state);
        }
        this.getNotesList(state).push(name);
    }

    getNotes(state) {
        if (!this.isValid(state)) {
            throw new Error('Invalid state ' + state);
        }
        return this.getNotesList(state);
    }

    getNotesList(state) {
        if (state === 'completed') {
            return completedNotes;
        } else if (state === 'active') {
            return activeNotes;
        }
        return otherNotes;
    }

    isValid(state) {
        return state === 'completed'
            || state === 'active'
            || state === 'others';
    }
}

// Test: Staff List
var staffs = [];

class StaffList {
    add(name, age){
        if(age > 20 && !this.isValid(name)){
            staffs.push(name);
        }else {
            throw new Error('Staff member age must be greater than 20');
        }
    }
    
    remove(name){
        if(this.isValid(name)){
            const idx = staffs.indexOf(name);
            if (idx > -1) staffs.splice(idx, 1);
            return true;
        }else{
            return false;
        }
    }
    
    getSize(){
        return staffs.length;
    }
    
    isValid(name) {
        return staffs.includes(name);
    }
}

