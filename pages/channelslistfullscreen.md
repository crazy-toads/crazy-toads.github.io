---
layout: fullscreen
permalink: /channelslist/fullscreen
title: Liste des canaux du Chat Fullscreen
linktitle: "Liste des canaux du Chat Fullscreen"
linkurl: /channelslist/fullscreen
description: "Liste des canaux du Chat https://coa.crapaud-fou.org"
jquery: true
cytoscape: true
vmap: true
style:  "#cy { width: 100%; height: 100%; position: fixed; }"
---
La molette de la souris sert à de/zoomer
<div id="cy"></div>
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
</script>
    
