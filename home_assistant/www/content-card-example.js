class ContentCardExample extends HTMLElement {
  set hass(hass) {
    if (!this.content) {
      const card = document.createElement('ha-card');
      card.header = 'Upcomming Events';
      this.content = document.createElement('div');
      this.content.style.padding = '0 16px 16px';
      card.appendChild(this.content);
      this.appendChild(card);
    }

    const entityId = this.config.entity;

    const state = hass.states[entityId];
    const calEntityId = 'senssor.events'
    const all_events = hass.states['sensor.events']['state'] 
    const eventlist = all_events.split('|')
    let  list_html = `
      <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            text-align: left;
            padding: 8px;
        }

        tr:nth-child(even){background-color: #f2f2f2}

        th {
            background-color: #4CAF50;
            color: white;
        }
      </style>`;

    list_html = list_html + ' <table style="width:100%"><tr><th>Event</th><th>Name</th><th>Date</th></tr>'
    const stateStr = state ? state.state : 'unavailable';
    for(var i = 0; i < eventlist.length; i++) {
      list_html = list_html + '<tr>'
      let each_event =  eventlist[i].split(':')
      console.log(each_event)
      
      for(var j = 0; j < 3; j++) {
        list_html = list_html + '<td>'
        list_html = list_html + each_event[j]
        list_html = list_html + '</td>'
      }
      
      list_html = list_html + '</tr>'
    }

    list_html = list_html + '</table>'
    console.log(list_html)
    
    this.content.innerHTML = list_html

  }

  setConfig(config) {
    if (!config.entity) {
      throw new Error('You need to define an entity');
    }
    this.config = config;
  }

  // The height of your card. Home Assistant uses this to automatically
  // distribute all cards over the available columns.
  getCardSize() {
    return 3;
  }
}

customElements.define('content-card-example', ContentCardExample);


