(function(){
    'use strict';
    window.addEventListener('load', function(){
        var forms = document.getElementsByClassName('needs-validation');
        var validation = Array.prototype.filter.call(forms, function(form){
            form.addEventListener('keyup', function(event){
                if (form.checkValidity() === false){
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
            form.addEventListener('submit', function(event){
                if (form.checkValidity() === false){
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

// These JQuery validations are for Email and Birthday fields to give AJAX responses as user types
$(document).ready(function(){
    $('#email').keyup(function(){
        let words = $(this)[0].value        // jquery "keyup" creates a list, as opposed to just a value, so we need to grab the [0] position's value
        $.ajax({
            method: "GET",
            url: "email_valid/"+words,
            success: function(serverResponse){
                $('#email_valid').html(serverResponse)      // put the serverResponse into the #email_valid section as html (comes from views.py)
            }
        })
    })

    $('#email').keyup(function(){
        let text = $(this)[0].value
        $.ajax({
            method: "GET",
            url: "email_regex/"+text,
            success: function(serverResponse){
                $('#email_regex').html(serverResponse)
            }
        })
    })

    $('#birthday').change(function(){
        console.log($(this)[0].value)
        let raw_date = $(this)[0].value
        $.ajax({
            method: "GET",
            url: "age_valid/"+raw_date,
            success: function(serverResponse){
                $('#birthday_valid').html(serverResponse)
            }
        })
    })
})

// JavaScript to compare passwords for custom validation:
var password = document.getElementById("password")
var password2 = document.getElementById("password2")
function validatePassword(){
    if (password.value != password2.value){
        password2.setCustomValidity("Passwords do not match: 8 chars min");
    }
    else {
        password2.setCustomValidity("");
    }
}
password.onchange = validatePassword;
password2.onkeyup = validatePassword;
