rooms = {
        'Hall' : {
            'desc' : 'Looks like a hallway. There\'s probably a dark secret or something.',
            'direction' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'north' : 'Foyer',
                'west' : 'Stairs'
                }
            },
        'Kitchen' : {
            'desc' : 'Normal kitchen-y things. Probably some knives with a twisted history...',
            'direction' : {
              'east' : 'Bar',
              'north' : 'Hall'
              },
            'item' : 'pizza'
            },
        'Bar' : {
            'desc' : 'A polished bar full of high-dollar beverages. Wonder what seedy means were used to acquire them...',
            'direction' : {
              'south' : 'Bathroom',
              'north' : 'Dining Room',
              'west' : 'Kitchen'
              },
            'item' : 'beer'
            },
        'Bathroom' : {
            'desc' : 'Full of the foul stench of corruption... (plus it\'s a bathroom)',
            'direction' : {
              'north' : 'Bar'
              }
            },
        'Dining Room' : {
            'desc' : 'This room lacks the personality of having been lived in by a loving family...',
            'direction' : {
              'south' : 'Bar',
              'north' : 'Porch',
              'west' : 'Hall'
              }
            },
        'Porch' : {
            'desc' : 'What a lovely spot to plan evil by moonlight...',
            'direction' : {
              'south' : 'Dining Room'
              }
            },
        'Foyer' : {
            'desc' : 'Perfect for welcoming the foulest of sorts...',
            'direction' : {
              'south' : 'Hall',
              'north' : 'Stoop'
              }
            },
        'Stoop' : {
            'desc' : 'Short stairs from normal to paranormal...',
            'direction' : {
              'south' : 'Foyer',
              'north' : 'path to leave'
              }
            },
        'Stairs' : {
            'desc' : 'Dark and creaky, dangerously narrow, stairs...',
            'direction' : {
              'east' : 'Hall',
              'upstairs' : 'Upstairs Hall'
              }
            },
        'Upstairs Hall' : {
            'desc' : 'A blank-slate of dark energy...',
            'direction' : {
              'south' : 'Bedroom',
              'east' : 'Master Bedroom'
              }
            },
        'Bedroom' : {
            'desc' : 'Likely last occupant? Death.',
            'direction' : {
              'north' : 'Upstairs Hall'
              }
            },
        'Master Bedroom' : {
            'desc' : 'No available bed, merely a row of coffins...',
            'direction' : {
              'west' : 'Upstairs Hall',
              'south' : 'Master Bathroom',
              'north' : 'Balcony'
              }
            },
        'Master Bathroom' : {
            'desc' : 'An inevitable necessity, regardless of the morality of your diet...',
            'direction' : {
              'north' : 'Master Bedroom'
              }
            },
        'Balcony' : {
            'desc' : 'A great spot to escape all of this troubling reality...',
            'direction' : {
              'south' : 'Master Bedroom'
              }
            }
        }


