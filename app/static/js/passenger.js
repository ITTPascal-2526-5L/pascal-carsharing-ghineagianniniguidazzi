$(document).ready(function() {
  console.log("JS caricato"); // Debug

  $.getJSON("/school", function(data) {
    console.log("JSON ricevuto:", data); // Debug

    $.each(data, function(index, item) {
      $("#SelectNomi").append(
        $("<option>", {
          value: item.id,  
          text: item.nome
        })
      );
    });
  }).fail(function(jqXHR, textStatus, errorThrown) {
    console.error("Errore caricamento JSON:", textStatus, errorThrown);
  });
});