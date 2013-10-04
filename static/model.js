function ViewModel()
{
    this.page = "";
    this.pages = "";
    this.previous = "";
    this.next = "";
}

// Activates knockout.js
ko.applyBindings(new AppViewModel());