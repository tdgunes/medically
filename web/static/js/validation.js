function isValid(input){
    input.val(input.val().trim())
    if(input.val() != "") return true
    else return false
}
function checkForm(mandatoryFields,button){
    for(var i=0;i<mandatoryFields.length;i++)
        if(!isValid(mandatoryFields[i])) {
            console.log((mandatoryFields[i]))
            return
        }
    button.removeAttr("disabled");
}

function validate(mandatoryFields, button){
    $(document).ready(function(){
        button.attr("disabled", "disabled")
        for(var i=0;i<mandatoryFields.length;i++){
            mandatoryFields[i].change(function() {
                checkForm(mandatoryFields,button)
            })
        }
    })
}