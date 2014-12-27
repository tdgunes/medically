function isValid(input){
    input.val(input.val().trim())
    if(input.val() != "") return true
    else return false
}
function disable(button) {
    button.attr("disabled", "disabled")
}
function checkForm(mandatoryFields,button){
    for(var i=0;i<mandatoryFields.length;i++)
        if(!isValid(mandatoryFields[i])) {
            disable(button)
            return
        }
    button.removeAttr("disabled");
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