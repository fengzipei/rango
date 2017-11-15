var checkme = document.getElementById('checker');
var userName = document.getElementById('name');
var userPhone = document.getElementById('phone');
var userEmail = document.getElementById('email');
var userPlace = document.getElementById('place');
var userSend = document.getElementById('submit');
var userQQ = document.getElementById('qq');
checkme.onchange = function () {
    userSend.disabled = !this.checked;
    userQQ.disabled = !this.checked;
    userName.disabled = !this.checked;
    userPhone.disabled = !this.checked;
    userEmail.disabled = !this.checked;
    userPlace.disabled = !this.checked;
};
