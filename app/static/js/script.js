$(document).ready(function() {
  $.getJSON("/json/school.json", function(data) {
    // data è un array di oggetti come [{nome: "Mario Rossi"}, ...]
    $.each(data, function(index, item) {
      $("#selectNomi").append(
        $("<option>", {
          value: item.nome,
          text: item.nome
        })
      );
    });
  }).fail(function() {
    console.error("Errore nel caricamento del file JSON.");
  });
});