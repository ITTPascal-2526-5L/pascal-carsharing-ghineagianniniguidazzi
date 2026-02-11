$(document).ready(function() {
  console.log("Documento pronto, caricamento scuole in corso...");
    const path ='app/json/school.json';
    console.log(`Provo percorso: ${path}`);
    {
    
    $.ajax({
      url: path,
      method: 'GET',
      dataType: 'json',
      success: function(data) {
        console.log(`✅ JSON caricato da: ${path}`, data);
        populateSchools(data);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log(`❌ Fallito: ${path}`, textStatus);
        // Prova il percorso successivo
        tryLoadJson(pathIndex + 1);
      }
    });
  }
  
  // Funzione per popolare le scuole
  function populateSchools(schools) {
    const select = $('#SelectNomi');
    
    if (!select.length) {
      console.error("Select #SelectNomi non trovato!");
      return;
    }
    
    // Rimuovi tutte le opzioni tranne la prima
    select.find('option:not(:first)').remove();
    
    // Controlla se ci sono scuole
    if (!schools || schools.length === 0) {
      console.warn("Nessuna scuola nel JSON");
      select.append('<option value="">Nessuna scuola disponibile</option>');
      return;
    }
    
    // Aggiungi ogni scuola
    schools.forEach(function(school, index) {
      // Gestisci diversi formati di JSON
      const schoolId = school.id || school.ID || school.codice || index;
      const schoolName = school.nome || school.Nome || school.name || `Scuola ${index + 1}`;
      
      select.append(`<option value="${schoolId}">${schoolName}</option>`);
    });
    
    console.log(`✅ Aggiunte ${schools.length} scuole`);
  }
  
  // Funzione per mostrare errore
  function showError(message) {
    const select = $('#SelectNomi');
    if (select.length) {
      select.append(`<option value="">${message}</option>`);
    }
    alert(message);
  }
  
  // Inizia il caricamento
  tryLoadJson(0)})
