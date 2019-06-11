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
    function UpdateMap(mapChoosen) {
        $('#vmap').replaceWith('<div id="vmap"></div>');
        $('#vmap').width('100%').height('800px').vectorMap({
            map: mapChoosen,
            backgroundColor: null,
            colors: regionsColor,
            hoverColor: 'yellowgreen',
            enableZoom: false,
            showTooltip: false,
            onRegionClick: function (element, code, region) {
                if (regionsClick[code] == null)
                    return;
                
                if (regionsClick[code]["updateMap"] != null) {
                    UpdateMap(regionsClick[code]["updateMap"]);
                } else {
                    window.open('https://coa.crapaud-fou.org/channel/'+regionsClick[code]["link"], '_blank');
                }                
            }
        });
    }

    $.getJSON("{{ site.baseurl }}/public/data/cohortescolor.json", function (datacolors){
        regionsColor = datacolors;
        UpdateMap('world_en');

        $.getJSON("{{ site.baseurl }}/public/data/cohorteslist.json", function (data){
            regionsClick = data; 
        });
    });
</script>
    
