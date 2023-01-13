
$(document).ready(function(){
    $(".filter1 input").change(function(){
        $(".filter1 input[type=submit]").click()
    })
    $(".drop_down select").change(function(){
        $(".drop_down input[type=submit]").click()
    })
})