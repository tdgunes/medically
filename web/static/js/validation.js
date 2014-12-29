function isValid(input){
    input.val(input.val().trim())
    if(input.val() != "") return true
    else return false
}
function disable(button) {
    button.attr("disabled", "disabled")
}
function enable(button) {
    button.removeAttr("disabled");
}
function checkForm(mandatoryFields,button){
    for(var i=0;i<mandatoryFields.length;i++)
        if(!isValid(mandatoryFields[i])) {
            disable(button)
            return
        }
    enable(button)
}

function checkRegisterform(mandatorFields, button, checkbox, email) {
    for (var i = 0; i < mandatoryFields.length; i++)
        if (!isValid(mandatoryFields[i])) {
            disable(button)
            return
        }
    enable(button);
}
function validate(mandatoryFields, button){
    $(document).ready(function(){
        checkForm(mandatoryFields, button)
        for(var i=0;i<mandatoryFields.length;i++){
            mandatoryFields[i].change(function() {
                checkForm(mandatoryFields,button)
            })
        }
    })
}
function isEmail(emailInput) {
    var email = emailInput.val()
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}
function validateEmail(email, symbol) {
    $(document).ready(function () {
        email.blur(function () {
            if (isEmail(email)) {
                symbol.removeClass('glyphicon-remove')
                symbol.addClass('glyphicon-ok')
            } else {
                symbol.removeClass('glyphicon-ok')
                symbol.addClass('glyphicon-remove')
            }
        })
    })
}