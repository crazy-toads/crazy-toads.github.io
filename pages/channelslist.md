---
layout: page
permalink: /channelslist/
title: Liste des canaux du Chat
linktitle: "Liste des canaux du Chat"
linkurl: /channelslist/
description: "Liste des canaux du Chat https://coa.crapaud-fou.org"
jquery: true
cytoscape: true
vmap: true
style:  "#cy { width: 100%; height: 500px; }"
---

Listes des canaux du [chat](https://coa.crapaud-fou.org) (aussi connu sous le nom de mare aux crapauds), rejoignez [nous](https://coa.crapaud-fou.org)
# Canaux de la mare
Les canaux permettent des discussions sur différents sujets  
Cliquez sur les canaux qui vous intéressent (la molette de le souris permet de zoomer)  
<a href="./fullscreen" target="_blank">Fullscreen</a>

<div id="cy"></div>

# Cohorte crapaud-fou en France
Les cohortes sont des groupements de crapauds dans une région  
Cliquez sur votre région

<div id="vmap"></div>

<script>
    var cy = cytoscape({
        container: document.getElementById('cy'),
        elements: $.getJSON("{{ site.baseurl }}/public/data/result.json"),
        style: [
            {
                selector: 'node',
                style: {
                    'label': 'data(label)',
                    'text-valign': 'center',
                    'background-color': 'data(color)',
                    'width': 'data(size)',
                    'height': 'data(size)',
                    'color': 'white',
                    'text-outline-width': 2,
                    'text-outline-color': '#888'
                }
            },
            {
                selector: 'edge',
                style: {
                    'line-color': 'data(color)'
                }
            }],
        layout: {
            name: 'cose',
            nodeDimensionsIncludeLabels: true,
            nodeOverlap: 50
        }
    });
    
    cy.on('tap', 'node', function () {
        try { // your browser may block popups
            window.open(this.data('href'));
        } catch (e) { // fall back on url change
            window.location.href = this.data('href');
        }
    });

    //TODO change this code to be generated
    regionsClick = { 'fr': function() { UpdateMap('france_fr'); },'fr-07': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-2607', '_blank') },'fr-26': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-2607', '_blank') },'fr-34': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-34', '_blank') },'be': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-belgique', '_blank') },'fr-21': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-bourgogne', '_blank') },'fr-58': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-bourgogne', '_blank') },'fr-71': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-bourgogne', '_blank') },'fr-89': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-bourgogne', '_blank') },'fr-22': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-bretagne', '_blank') },'fr-29': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-bretagne', '_blank') },'fr-35': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-bretagne', '_blank') },'fr-56': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-bretagne', '_blank') },'fr-18': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-centre', '_blank') },'fr-28': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-centre', '_blank') },'fr-36': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-centre', '_blank') },'fr-37': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-centre', '_blank') },'fr-41': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-centre', '_blank') },'fr-45': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-centre', '_blank') },'fr-08': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-grand-est', '_blank') },'fr-10': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-grand-est', '_blank') },'fr-51': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-grand-est', '_blank') },'fr-52': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-grand-est', '_blank') },'fr-54': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-grand-est', '_blank') },'fr-55': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-grand-est', '_blank') },'fr-57': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-grand-est', '_blank') },'fr-67': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-grand-est', '_blank') },'fr-68': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-grand-est', '_blank') },'fr-88': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-grand-est', '_blank') },'fr-38': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-grenoble', '_blank') },'fr-02': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-hdf', '_blank') },'fr-59': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-hdf', '_blank') },'fr-60': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-hdf', '_blank') },'fr-62': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-hdf', '_blank') },'fr-80': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-hdf', '_blank') },'fr-75': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-ile-de-france', '_blank') },'fr-77': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-ile-de-france', '_blank') },'fr-78': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-ile-de-france', '_blank') },'fr-91': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-ile-de-france', '_blank') },'fr-92': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-ile-de-france', '_blank') },'fr-93': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-ile-de-france', '_blank') },'fr-94': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-ile-de-france', '_blank') },'fr-95': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-ile-de-france', '_blank') },'re': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-la-reunion', '_blank') },'fr-14': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-normandie', '_blank') },'fr-27': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-normandie', '_blank') },'fr-50': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-normandie', '_blank') },'fr-61': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-normandie', '_blank') },'fr-76': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-normandie', '_blank') },'fr-04': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-paca', '_blank') },'fr-05': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-paca', '_blank') },'fr-06': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-paca', '_blank') },'fr-13': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-paca', '_blank') },'fr-83': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-paca', '_blank') },'fr-84': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-paca', '_blank') },'fr-74': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-paysdesavoie', '_blank') },'fr-73': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-paysdesavoie', '_blank') },'fr-09': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-12': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-24': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-31': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-32': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-33': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-40': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-46': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-47': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-64': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-65': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-81': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'fr-82': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-sud-ouest', '_blank') },'ch': function() { window.open('https://coa.crapaud-fou.org/channel/cohorte-suisse', '_blank') }, };
    function UpdateMap(mapChoosen) {
        $('#vmap').replaceWith('<div id="vmap"></div>');
        $('#vmap').width('100%').height('800px').vectorMap({
            map: mapChoosen,
            backgroundColor: null,
            colors: { 'fr':'green','fr-07':'green','fr-26':'green','fr-34':'green','be':'green','fr-21':'green','fr-58':'green','fr-71':'green','fr-89':'green','fr-22':'green','fr-29':'green','fr-35':'green','fr-56':'green','fr-18':'green','fr-28':'green','fr-36':'green','fr-37':'green','fr-41':'green','fr-45':'green','fr-08':'green','fr-10':'green','fr-51':'green','fr-52':'green','fr-54':'green','fr-55':'green','fr-57':'green','fr-67':'green','fr-68':'green','fr-88':'green','fr-38':'green','fr-02':'green','fr-59':'green','fr-60':'green','fr-62':'green','fr-80':'green','fr-75':'green','fr-77':'green','fr-78':'green','fr-91':'green','fr-92':'green','fr-93':'green','fr-94':'green','fr-95':'green','re':'green','fr-14':'green','fr-27':'green','fr-50':'green','fr-61':'green','fr-76':'green','fr-04':'green','fr-05':'green','fr-06':'green','fr-13':'green','fr-83':'green','fr-84':'green','fr-74':'green','fr-73':'green','fr-09':'green','fr-12':'green','fr-24':'green','fr-31':'green','fr-32':'green','fr-33':'green','fr-40':'green','fr-46':'green','fr-47':'green','fr-64':'green','fr-65':'green','fr-81':'green','fr-82':'green','ch':'green', },
            hoverColor: 'yellowgreen',
            enableZoom: false,
            showTooltip: false,
            onRegionClick: function (element, code, region) {
                regionsClick[code]();
            }
        });
    }

    UpdateMap('world_en');
</script>
    
