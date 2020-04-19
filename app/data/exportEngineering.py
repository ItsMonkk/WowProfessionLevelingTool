#!/usr/bin/env python3.7

recipes = {
    "Accurate Scope": {
        "ID":       4407,
        "Learn":    180,
        "Yellow":   200,
        "Green":    210,
        "Grey":     220,
        "Source":   "Vendor",
        "Reagents": {
			"Bronze Tube": 1,
			"Jade": 1,
			"Citrine": 1
        }
    },
	"Advanced Target Dummy": {
        "ID":       4392,
        "Learn":    185,
        "Yellow":   185,
        "Green":    205,
        "Grey":     225,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Strut": 1,
			"Bronze Framework": 1,
			"Gyrochronatom": 1,
			"Heavy Leather": 4
        }
    },
	"Alarm-O-Bot": {
        "ID":       18645,
        "Learn":    265,
        "Yellow":   275,
        "Green":    280,
        "Grey":     285,
        "Source":   "Drop",
        "RecipeID": 18654,
		"School": "Gnomish",
        "Reagents": {
			"Thorium Bar": 4,
			"Thorium Widget": 2,
			"Rugged Leather": 4,
			"Star Ruby": 1,
			"Fused Wiring": 1
        }
    },
	"Aquadynamic Fish Attractor": {
        "ID":       6533,
        "Learn":    150,
        "Yellow":   150,
        "Green":    160,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Bar": 2,
			"Nightcrawlers": 1,
			"Coarse Blasting Powder": 1
        }
    },
	"Arclight Spanner": {
        "ID":       6219,
        "Learn":    50,
        "Yellow":   70,
        "Green":    80,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Bar": 6
        }
    },
	"Big Bronze Bomb": {
        "ID":       4380,
        "Learn":    140,
        "Yellow":   140,
        "Green":    165,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Blasting Powder": 2,
			"Bronze Bar": 3,
			"Silver Contact": 1
        }
    },
	"Big Iron Bomb": {
        "ID":       4394,
        "Learn":    190,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Bar": 3,
			"Heavy Blasting Powder": 3,
			"Silver Contact": 1
        }
    },
	"Blue Firework": {
        "ID":       9312,
        "Learn":    150,
        "Yellow":   150,
        "Green":    162,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Blue Rocker Cluster": {
        "ID":       21571,
        "Learn":    225,
        "Yellow":   225,
        "Green":    237,
        "Grey":     250,
        "Source":   "Seasonal",
        "Reagents": {
			"Solid Blasting Powder": 1,
			"Thick Leather": 1
        }
    },
	"Bright-Eye Googles": {
        "ID":       10499,
        "Learn":    175,
        "Yellow":   195,
        "Green":    205,
        "Grey":     215,
        "Source":   "Drop",
        "RecipeID": 10601,
        "Reagents": {
			"Heavy Leather": 6,
			"Citrine": 2
        }
    },
	"Bronze Framework": {
        "ID":       4382,
        "Learn":    145,
        "Yellow":   145,
        "Green":    170,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Bar": 2,
			"Medium Leather": 1,
			"Wool Cloth": 1
        }
    },
	"Bronze Tube": {
        "ID":       4371,
        "Learn":    105,
        "Yellow":   105,
        "Green":    130,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Bar": 2,
			"Weak Flux": 1
        }
    },
	"Catseye Ultra Googles": {
        "ID":       10501,
        "Learn":    220,
        "Yellow":   240,
        "Green":    250,
        "Grey":     260,
        "Source":   "Drop",
        "RecipeID": 10603,
        "Reagents": {
			"Thick Leather": 4,
			"Aquamarine": 2,
			"Catseye Elixir": 1
        }
    },
	"Coarse Blasting Powder": {
        "ID":       4364,
        "Learn":    75,
        "Yellow":   85,
        "Green":    90,
        "Grey":     95,
        "Source":   "Trainer",
        "Reagents": {
			"Coarse Stone": 1
        }
    },
	"Coarse Dynamite": {
        "ID":       4365,
        "Learn":    75,
        "Yellow":   90,
        "Green":    97,
        "Grey":     105,
        "Source":   "Trainer",
        "Reagents": {
			"Coarse Blasting Powder": 3,
			"Linen Cloth": 1
        }
    },
	"Compact Harvest Reaper Kit": {
        "ID":       4391,
        "Learn":    175,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Strut": 2,
			"Bronze Framework": 1,
			"Gyrochronatom": 2,
			"Heavy Leather": 4
        }
    },
	"Copper Modulator": {
        "ID":       4363,
        "Learn":    65,
        "Yellow":   95,
        "Green":    110,
        "Grey":     125,
        "Source":   "Trainer",
        "Reagents": {
			"Handful of Copper Bolts": 2,
			"Copper Bar": 1,
			"Linen Cloth": 2
        }
    },
	"Copper Tube": {
        "ID":       4361,
        "Learn":    50,
        "Yellow":   80,
        "Green":    95,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Bar": 2,
			"Weak Flux": 1
        }
    },
	"Crafted Heavy Shot": {
        "ID":       8068,
        "Learn":    75,
        "Yellow":   85,
        "Green":    90,
        "Grey":     95,
        "Source":   "Trainer",
        "Reagents": {
			"Coarse Blasting Powder": 1,
			"Copper Bar": 1
        }
    },
	"Crafted Light Shot": {
        "ID":       8067,
        "Learn":    1,
        "Yellow":   30,
        "Green":    45,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
			"Rough Blasting Powder": 1,
			"Copper Bar": 1
        }
    },
	"Crafted Solid Shot": {
        "ID":       8069,
        "Learn":    125,
        "Yellow":   125,
        "Green":    135,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Bronze Bar": 1
        }
    },
	"Craftmans Monocle": {
        "ID":       4393,
        "Learn":    185,
        "Yellow":   205,
        "Green":    215,
        "Grey":     225,
        "Source":   "Drop",
        "RecipeID": 4415,
        "Reagents": {
			"Heavy Leather": 6,
			"Citrine": 2
        }
    },
	"Crude Scope": {
        "ID":       4405,
        "Learn":    60,
        "Yellow":   90,
        "Green":    105,
        "Grey":     120,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Tube": 1,
			"Malachite": 1,
			"Handful of Copper Bolts": 1
        }
    },
	"Dark Iron Bomb": {
        "ID":       16005,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 16049,
        "Reagents": {
			"Thorium Widget": 2,
			"Dark Iron Bar": 1,
			"Dense Blasting Powder": 3,
			"Runecloth": 3
        }
    },
	"Dark Iron Rifle": {
        "ID":       16004,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Drop",
        "RecipeID": 16048,
        "Reagents": {
			"Thorium Tube": 2,
			"Dark Iron Bar": 6,
			"Deadly Scope": 2,
			"Blue Sapphire": 2,
			"Large Opal": 2,
			"Rugged Leather": 4
        }
    },
	"Deadly Blunderbuss": {
        "ID":       4369,
        "Learn":    105,
        "Yellow":   130,
        "Green":    142,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Tube": 2,
			"Handful of Copper Bolts": 4,
			"Wooden Stock": 1,
			"Medium Leather": 2
        }
    },
	"Deadly Scope": {
        "ID":       10546,
        "Learn":    210,
        "Yellow":   230,
        "Green":    240,
        "Grey":     250,
        "Source":   "Vendor",
        "Reagents": {
			"Mithril Tube": 1,
			"Aquamarine": 2,
			"Thick Leather": 2
        }
    },
	"Deepdive Helmet": {
        "ID":       10506,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Vendor",
        "Reagents": {
			"Mithril Bar": 8,
			"Mithril Casing": 1,
			"Truesilver Bar": 1,
			"Tigerseye": 4,
			"Malachite": 4
        }
    },
	"Delicate Arcanite Converter": {
        "ID":       16006,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Vendor",
        "Reagents": {
			"Arcanite Bar": 1,
			"Ironweb Spider Silk": 1
        }
    },
	"Dense Blasting Powder": {
        "ID":       15992,
        "Learn":    250,
        "Yellow":   250,
        "Green":    255,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
			"Dense Stone": 2
        }
    },
	"Dense Dynamite": {
        "ID":       18641,
        "Learn":    250,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
			"Dense Blasting Powder": 2,
			"Runecloth": 3
        }
    },
	"Dimensoinal Ripper - Everlook": {
        "ID":       18984,
        "Learn":    260,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Bar": 10,
			"Truesilver Transformer": 1,
			"Heart of Fire": 4,
			"Star Ruby": 2,
			"The Big One": 1
        }
    },
	"Discombobulator Ray": {
        "ID":       4388,
        "Learn":    160,
        "Yellow":   180,
        "Green":    190,
        "Grey":     200,
        "Source":   "Drop",
        "RecipeID": 4413,
        "Reagents": {
			"Whirring Bronze Gizmo": 3,
			"Silk Cloth": 2,
			"Jade": 1,
			"Bronze Tube": 1
        }
    },
	"Explosive Sheep": {
        "ID":       4384,
        "Learn":    150,
        "Yellow":   175,
        "Green":    187,
        "Grey":     200,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Framework": 1,
			"Whirring Bronze Gizmo": 1,
			"Heavy Blasting Powder": 2,
			"Wool Cloth": 2
        }
    },
	"EZ-Thro Dynamite": {
        "ID":       6714,
        "Learn":    100,
        "Yellow":   115,
        "Green":    122,
        "Grey":     130,
        "Source":   "Drop",
        "RecipeID": 6716,
        "Reagents": {
			"Coarse Blasting Powder": 4,
			"Wool Cloth": 1
        }
    },
	"EZ-Thro Dynamite II": {
        "ID":       18588,
        "Learn":    200,
        "Yellow":   200,
        "Green":    210,
        "Grey":     220,
        "Source":   "Vendor",
        "Reagents": {
			"Solid Blasting Powder": 1,
			"Mageweave Cloth": 2
        }
    },
	"Fire Googles": {
        "ID":       10500,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
        "Reagents": {
			"Green Tinted Googles": 1,
			"Citrine": 2,
			"Elemental Fire": 2,
			"Heavy Leather": 4
        }
    },
	"Firework Cluster Launcher": {
        "ID":       21570,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Seasonal",
        "Reagents": {
			"Inlaid Mithril Cylinder": 4,
			"Goblin Rocket Fuel": 4,
			"Truesilver Transformer": 2,
			"Mithril Casing": 1
        }
    },
	"Firework Launcher": {
        "ID":       21569,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Seasonal",
        "Reagents": {
			"Inlaid Mithril Cylinder": 1,
			"Goblin Rocket Fuel": 1,
			"Unstable Trigger": 1,
			"Mithril Casing": 1
        }
    },
	"Flame Deflector": {
        "ID":       4376,
        "Learn":    125,
        "Yellow":   125,
        "Green":    150,
        "Grey":     175,
        "Source":   "Drop",
        "RecipeID": 4411,
        "Reagents": {
			"Whirring Bronze Gizmo": 1,
			"Small Flame Sac": 1 
        }
    },
	"Flash Bomb": {
        "ID":       4852,
        "Learn":    185,
        "Yellow":   185,
        "Green":    205,
        "Grey":     225,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
			"Blue Pearl": 1,
			"Heavy Blasting Powder": 1,
			"Silk Cloth": 1
        }
    },
	"Flying Tiger Googles": {
        "ID":       4368,
        "Learn":    100,
        "Yellow":   130,
        "Green":    145,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 6,
			"Tigerseye": 2
        }
    },
	"Gnomish Battle Chicken": {
        "ID":       10725,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Casing": 1,
			"Truesilver Bar": 6,
			"Mithril Bar": 6,
			"Inlaid Mithril Cylinder": 2,
			"Gold Power Core": 1,
			"Jade": 1
        }
    },
	"Gnomish Cloaking Device": {
        "ID":       4397,
        "Learn":    200,
        "Yellow":   220,
        "Green":    230,
        "Grey":     240,
        "Source":   "Vendor",
        "Reagents": {
			"Gyrochronatom": 4,
			"Jade": 2,
			"Lesser Moonstone": 2,
			"Citrine": 2,
			"Fused Wiring": 1
        }
    },
	"Gnomish Death Ray": {
        "ID":       10645,
        "Learn":    240,
        "Yellow":   260,
        "Green":    270,
        "Grey":     280,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Tube": 2,
			"Unstable Trigger": 1,
			"Essence of Undeath": 1,
			"Ichor of Undeath": 4,
			"Inlaid Mithril Cylinder": 1
        }
    },
	"Gnomish Goggles": {
        "ID":       10545,
        "Learn":    210,
        "Yellow":   230,
        "Green":    240,
        "Grey":     250,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Fire Goggles": 1,
			"Mithril Tube": 1,
			"Gold Power Core": 2,
			"Flask of Mojo": 2,
			"Heavy Leather": 2
        }
    },
	"Gnomish Harm Prevention Belt": {
        "ID":       10721,
        "Learn":    215,
        "Yellow":   235,
        "Green":    245,
        "Grey":     255,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Dusky Belt": 1,
			"Mithril Bar": 4,
			"Truesilver Bar": 2,
			"Unstable Trigger": 1,
			"Aquamarine": 2
        }
    },
	"Gnomish Mind Control Cap": {
        "ID":       10726,
        "Learn":    235,
        "Yellow":   255,
        "Green":    265,
        "Grey":     275,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Bar": 10,
			"Truesilver Bar": 4,
			"Gold Power Core": 1,
			"Star Ruby": 2,
			"Mageweave Cloth": 4
        }
    },
	"Gnomish Net-o-Matic Projector": {
        "ID":       10720,
        "Learn":    210,
        "Yellow":   230,
        "Green":    240,
        "Grey":     250,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Tube": 1,
			"Shadow Silk": 2,
			"Thick Spiders Silk": 4,
			"Solid Blasting Powder": 2,
			"Mithril Bar": 4
        }
    },
	"Gnomish Rocket Boots": {
        "ID":       10724,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Black Mageweave Boots": 1,
			"Mithril Tube": 2,
			"Heavy Leather": 4,
			"Solid Blasting Powder": 8,
			"Gyrochronatom": 4
        }
    },
	"Gnomish Shrink Ray": {
        "ID":       10716,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Tube": 1,
			"Unstable Trigger": 1,
			"Mithril Bar": 4,
			"Flask of Mojo": 4,
			"Jade": 2
        }
    },
	"Gnomish Universal Remote": {
        "ID":       7506,
        "Learn":    125,
        "Yellow":   150,
        "Green":    162,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
			"Bronze Bar": 6,
			"Whirring Bronze Gizmo": 1,
			"Flask of Oil": 2,
			"Tigerseye": 1,
			"Malachite": 1
        }
    },
	"Goblin Bomb Dispenser": {
        "ID":       10587,
        "Learn":    230,
        "Yellow":   230,
        "Green":    250,
        "Grey":     270,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Casing": 2,
			"Solid Blasting Powder": 4,
			"Truesilver Bar": 6,
			"Unstable Trigger": 1,
			"Accurate Scope": 2
        }
    },
	"Goblin Construction Helmet": {
        "ID":       10543,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Bar": 8,
			"Citrine": 1,
			"Elemental Fire": 4
        }
    },
	"Goblin Dragon Gun": {
        "ID":       10727,
        "Learn":    240,
        "Yellow":   260,
        "Green":    270,
        "Grey":     280,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Tube": 2,
			"Goblin Rocket Fuel": 4,
			"Mithril Bar": 6,
			"Truesilver Bar": 6,
			"Unstable Trigger": 1
        }
    },
	"Goblin Jumper Cables": {
        "ID":       7148,
        "Learn":    165,
        "Yellow":   165,
        "Green":    180,
        "Grey":     200,
        "Source":   "Vendor",
        "Reagents": {
			"Iron Bar": 6,
			"Whirring Bronze Gizmo": 2,
			"Flask of Oil": 2,
			"Silk Cloth": 2,
			"Shadowgem": 2,
			"Fused Wiring": 1
        }
    },
	"Goblin Jumper Cables XL": {
        "ID":       18587,
        "Learn":    265,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Drop",
        "RecipeID": 18653,
        "Reagents": {
			"Thorium Widget": 2,
			"Truesilver Transformer": 2,
			"Fused Wiring": 2,
			"Ironweb Spider Silk": 2,
			"Star Ruby": 2
        }
    },
	"Goblin Land Mine": {
        "ID":       4395,
        "Learn":    195,
        "Yellow":   215,
        "Green":    225,
        "Grey":     235,
        "Source":   "Drop",
        "RecipeID": 4416,
        "Reagents": {
			"Heavy Blasting Powder": 3,
			"Iron Bar": 2,
			"Gyrochronatom": 1
        }
    },
	"Goblin Mining Helmet": {
        "ID":       10542,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Bar": 8,
			"Citrine": 1,
			"Elemental Earth": 4
        }
    },
	"Goblin Mortar": {
        "ID":       10577,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
		"School":	"Golbin",
        "Reagents": {
			"Mithril Tube": 2,
			"Mithril Bar": 4,
			"Solid Blasting Powder": 5,
			"Gold Power Core": 1,
			"Elemental Fire": 1
        }
    },
	"Goblin Rocket Boots": {
        "ID":       7189,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Black Mageweave Boots": 1,
			"Mithril Tube": 2,
			"Heavy Leather": 4,
			"Goblin Rocket Fuel": 2,
			"Unstable Trigger": 1
        }
    },
	"Goblin Rocket Fuel Recipe": {
        "ID":       10644,
        "Learn":    205,
        "Yellow":   205,
        "Green":    205,
        "Grey":     205,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Blank Parchment": 1,
			"Engineers Ink": 1
        }
    },
	"Goblin Rocket Helmet": {
        "ID":       10588,
        "Learn":    245,
        "Yellow":   265,
        "Green":    275,
        "Grey":     285,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Goblin Construction Helmet": 1,
			"Goblin Rocket Fuel": 4,
			"Mithril Bar": 4,
			"Unstable Trigger": 1
        }
    },
	"Goblin Sapper Charge": {
        "ID":       10646,
        "Learn":    205,
        "Yellow":   205,
        "Green":    225,
        "Grey":     245,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mageweave Cloth": 1,
			"Solid Blasting Powder": 3,
			"Unstable Trigger": 1
        }
    },
	"Gold Power Core": {
        "ID":       1210558584,
        "Learn":    150,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
			"Gold Bar": 1
        }
    },
	"Green Firework": {
        "ID":       9313,
        "Learn":    150,
        "Yellow":   150,
        "Green":    162,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Green Lens": {
        "ID":       10504,
        "Learn":    245,
        "Yellow":   265,
        "Green":    275,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 8,
			"Jade": 3,
			"Aquamarine": 3,
			"Heart of the Wild": 2,
			"Wildvine": 2
        }
    },
	"Green Rocket Cluster": {
        "ID":       21574,
        "Learn":    225,
        "Yellow":   225,
        "Green":    237,
        "Grey":     250,
        "Source":   "Seasonal",
        "Reagents": {
			"Solid Blasting Powder": 1,
			"Thick Leather": 1
        }
    },
	"Green Tinted Goggles": {
        "ID":       4385,
        "Learn":    150,
        "Yellow":   175,
        "Green":    187,
        "Grey":     200,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Leather": 4,
			"Moss Agate": 2,
			"Flying Tiger Goggles": 1
        }
    },
	"Gyrochronatom": {
        "ID":       4389,
        "Learn":    170,
        "Yellow":   170,
        "Green":    190,
        "Grey":     210,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Bar": 1,
			"Gold Power Core": 1
        }
    },
	"Gyrofreeze Ice Reflector": {
        "ID":       18634,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Vendor",
        "Reagents": {
			"Thorium Widget": 6,
			"Truesilver Transformer": 2,
			"Blue Sapphire": 2,
			"Essence of Fire": 4,
			"Frost Oil": 2,
			"Icecap": 4
        }
    },
	"Gyromatic Micro-Adjustor": {
        "ID":       10498,
        "Learn":    175,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Steel Bar": 4
        }
    },
	"Handful of Copper Bolts": {
        "ID":       4359,
        "Learn":    30,
        "Yellow":   45,
        "Green":    52,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Bar": 1
        }
    },
	"Heavy Blasting Powder": {
        "ID":       4377,
        "Learn":    125,
        "Yellow":   125,
        "Green":    135,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Stone": 1
        }
    },
	"Heavy Dynamite": {
        "ID":       4378,
        "Learn":    125,
        "Yellow":   125,
        "Green":    135,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Blasting Powder": 2,
			"Wool Cloth": 1
        }
    },
	"Hi-Explosive Bomb": {
        "ID":       10562,
        "Learn":    235,
        "Yellow":   235,
        "Green":    255,
        "Grey":     275,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Casing": 2,
			"Unstable Trigger": 1,
			"Solid Blasting Powder": 2
        }
    },
	"Hi-Impact Mithril Slugs": {
        "ID":       10512,
        "Learn":    210,
        "Yellow":   210,
        "Green":    230,
        "Grey":     250,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 1,
			"Solid Blasting Powder": 1
        }
    },
	"Hyper-Radiant Flame Reflector": {
        "ID":       18638,
        "Learn":    290,
        "Yellow":   210,
        "Green":    320,
        "Grey":     330,
        "Source":   "Drop",
        "RecipeID": 18657,
        "Reagents": {
			"Dark Iron Bar": 4,
			"Truesilver Transformer": 3,
			"Essence of Water": 6,
			"Star Ruby": 4,
			"Azerothian Diamond": 2
        }
    },
	"Ice Deflector": {
        "ID":       4386,
        "Learn":    155,
        "Yellow":   175,
        "Green":    185,
        "Grey":     195,
        "Source":   "Vendor",
		"Reagents": {
			"Whirring Bronze Gizmo": 1,
			"Frost Oil": 1
        }
    },
	"Inlaid Mithril Cylinder Plans": {
        "ID":       10713,
        "Learn":    205,
        "Yellow":   205,
        "Green":    205,
        "Grey":     205,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Blank Parchment": 1,
			"Engineers Ink": 1
        }
    },
	"Iron Grenade": {
        "ID":       4390,
        "Learn":    175,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Bar": 1,
			"Heavy Blasting Powder": 1,
			"Silk Cloth": 1
        }
    },
	"Iron Strut": {
        "ID":       4387,
        "Learn":    160,
        "Yellow":   160,
        "Green":    170,
        "Grey":     180,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Bar": 2
        }
    },
	"Large Blue Rocket": {
        "ID":       21589,
        "Learn":    175,
        "Yellow":   175,
        "Green":    187,
        "Grey":     200,
        "Source":   "Seasonal",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Large Blue Rocket Cluster": {
        "ID":       21714,
        "Learn":    275,
        "Yellow":   275,
        "Green":    280,
        "Grey":     285,
        "Source":   "Seasonal",
        "Reagents": {
			"Dense Blasting Powder": 1,
			"Rugged Leather": 1
        }
    },
	"Large Copper Bomb": {
        "ID":       4370,
        "Learn":    105,
        "Yellow":   105,
        "Green":    130,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Bar": 3,
			"Coarse Blasting Powder": 4,
			"Silver Contact": 1
        }
    },
	"Large Green Rocket": {
        "ID":       21590,
        "Learn":    175,
        "Yellow":   175,
        "Green":    187,
        "Grey":     200,
        "Source":   "Seasonal",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Large Green Rocket Cluster": {
        "ID":       21716,
        "Learn":    275,
        "Yellow":   275,
        "Green":    280,
        "Grey":     285,
        "Source":   "Seasonal",
        "Reagents": {
			"Dense Blasting Powder": 1,
			"Rugged Leather": 1
        }
    },
	"Large Red Rocket": {
        "ID":       21592,
        "Learn":    175,
        "Yellow":   175,
        "Green":    187,
        "Grey":     200,
        "Source":   "Seasonal",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Large Red Rocket Cluster": {
        "ID":       21718,
        "Learn":    275,
        "Yellow":   275,
        "Green":    280,
        "Grey":     285,
        "Source":   "Seasonal",
        "Reagents": {
			"Dense Blasting Powder": 1,
			"Rugged Leather": 1
        }
    },
	"Large Seaforium Charge": {
        "ID":       4398,
        "Learn":    200,
        "Yellow":   200,
        "Green":    220,
        "Grey":     240,
        "Source":   "Drop",
        "RecipeID": 4417,
        "Reagents": {
			"Solid Blasting Powder": 2,
			"Heavy Leather": 2,
			"Refreshing Spring Water": 1
        }
    },
	"Lifelike Mechanical Toad": {
        "ID":       15996,
        "Learn":    265,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Drop",
        "RecipeID": 16044,
        "Reagents": {
			"Living Essence": 1,
			"Thorium Widget": 4,
			"Gold Power Core": 1,
			"Rugged Leather": 1
        }
    },
	"Lil Smoky": {
        "ID":       11826,
        "Learn":    205,
        "Yellow":   205,
        "Green":    205,
        "Grey":     205,
        "Source":   "Quest",
        "Faction":  "Any",
		"School":	"Gnomish",
        "Reagents": {
			"Core of Earth": 1,
			"Gyrochronatom": 2,
			"Fused Wiring": 1,
			"Mithril Bar": 2,
			"Truesilver Bar": 1
        }
    },
	"Lovingly Crafted Boomstick": {
        "ID":       4372,
        "Learn":    120,
        "Yellow":   145,
        "Green":    157,
        "Grey":     170,
        "Source":   "Vendor",
        "Reagents": {
			"Bronze Tube": 2,
			"Handful of Copper Bolts": 2,
			"Heavy Stock": 1,
			"Moss Agate": 3
        }
    },
	"Major Recombobulator": {
        "ID":       18637,
        "Learn":    275,
        "Yellow":   285,
        "Green":    290,
        "Grey":     295,
        "Source":   "Drop",
        "RecipeID": 18655,
        "Reagents": {
			"Thorium Tube": 2,
			"Truesilver Transformer": 1,
			"Runecloth": 2
        }
    },
	"Master Engineers Goggles": {
        "ID":       16008,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Drop",
        "RecipeID": 16053,
        "Reagents": {
			"Fire Goggles": 1,
			"Huge Emerald": 2,
			"Enchanted Leather": 4
        }
    },
	"Masterwork Target Dummy": {
        "ID":       16023,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Vendor",
        "Reagents": {
			"Mithril Casing": 1,
			"Thorium Tube": 1,
			"Thorium Widget": 2,
			"Truesilver Bar": 1,
			"Rugged Leather": 2,
			"Runecloth": 4
        }
    },
	"Mechanical Dragonling": {
        "ID":       4396,
        "Learn":    200,
        "Yellow":   220,
        "Green":    230,
        "Grey":     240,
        "Source":   "Vendor",
        "Reagents": {
			"Bronze Framework": 1,
			"Iron Strut": 4,
			"Gyrochronatom": 4,
			"Citrine": 2,
			"Fused Wiring": 1
        }
    },
	"Mechanical Repair Kit": {
        "ID":       11590,
        "Learn":    200,
        "Yellow":   200,
        "Green":    220,
        "Grey":     240,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 1,
			"Mageweave Cloth": 1,
			"Solid Blasting Powder": 1
        }
    },
	"Mechanical Squirrel": {
        "ID":       4401,
        "Learn":    75,
        "Yellow":   105,
        "Green":    120,
        "Grey":     135,
        "Source":   "Drop",
        "RecipeID": 4408,
        "Reagents": {
			"Copper Modulator": 1,
			"Handful of Copper Bolts": 1,
			"Copper Bar": 1,
			"Malachite": 2
        }
    },
	"Minor Recombobulator": {
        "ID":       4381,
        "Learn":    140,
        "Yellow":   165,
        "Green":    177,
        "Grey":     190,
        "Source":   "Vendor",
        "Reagents": {
			"Bronze Tube": 1,
			"Whirring Bronze Gizmo": 2,
			"Medium Leather": 2,
			"Moss Agate": 1
        }
    },
	"Mithril Blunderbuss": {
        "ID":       10508,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Tube": 1,
			"Unstable Trigger": 1,
			"Heavy Stock": 1,
			"Mithril Bar": 4,
			"Elemental Fire": 2
        }
    },
	"Mithril Casing": {
        "ID":       10561,
        "Learn":    215,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 3
        }
    },
	"Mithril Frag Bomb": {
        "ID":       10514,
        "Learn":    215,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Casing": 1,
			"Unstable Trigger": 1,
			"Solid Blasting Powder": 1
        }
    },
	"Mithril Gyro-Shot": {
        "ID":       10513,
        "Learn":    245,
        "Yellow":   245,
        "Green":    265,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 2,
			"Solid Blasting Powder": 2
        }
    },
	"Mithril Heavy-bore Rifle": {
        "ID":       10510,
        "Learn":    220,
        "Yellow":   240,
        "Green":    250,
        "Grey":     260,
        "Source":   "Drop",
        "RecipeID": 10604,
        "Reagents": {
			"Mithril Tube": 2,
			"Unstable Trigger": 1,
			"Heavy Stock": 1,
			"Mithril Bar": 6,
			"Citrine": 2
        }
    },
	"Mithril Mechanical Dragonling": {
        "ID":       10576,
        "Learn":    250,
        "Yellow":   270,
        "Green":    280,
        "Grey":     290,
        "Source":   "Vendor",
        "Reagents": {
			"Mithril Bar": 14,
			"Heart of Fire": 4,
			"Truesilver Bar": 4,
			"Inlaid Mithril Cylinder": 2,
			"Goblin Rocket Fuel": 2,
			"Star Ruby": 2
        }
    },
	"Mithril Tube": {
        "ID":       10559,
        "Learn":    195,
        "Yellow":   195,
        "Green":    215,
        "Grey":     235,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 3
        }
    },
	"Moonsight Rifle": {
        "ID":       4383,
        "Learn":    145,
        "Yellow":   170,
        "Green":    182,
        "Grey":     195,
        "Source":   "Drop",
        "RecipeID": 4412,
        "Reagents": {
			"Bronze Tube": 3,
			"Whirring Bronze Gizmo": 3,
			"Heavy Stock": 1,
			"Lesser Moonstone": 2
        }
    },
	"Ornate Spyglass": {
        "ID":       5507,
        "Learn":    135,
        "Yellow":   160,
        "Green":    172,
        "Grey":     185,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Tube": 2,
			"Whirring Bronze Gizmo": 2,
			"Copper Modulator": 1,
			"Moss Agate": 1
        }
    },
	"Parachute Cloak": {
        "ID":       10518,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Drop",
        "RecipeID": 10606,
        "Reagents": {
			"Bolt of Mageweave": 4,
			"Shadow Silk": 2,
			"Unstable Trigger": 1,
			"Solid Blasting Powder": 4
        }
    },
	"Pet Bombling": {
        "ID":       11825,
        "Learn":    205,
        "Yellow":   205,
        "Green":    205,
        "Grey":     205,
        "Source":   "Quest",
        "Faction":  "Any",
		"School":	"Goblin",
        "Reagents": {
			"Big Iron Bomb": 1,
			"Heart of Fire": 1,
			"Fused Wiring": 1,
			"Mithril Bar": 6
        }
    },
	"Portable Bronze Mortar": {
        "ID":       4403,
        "Learn":    165,
        "Yellow":   185,
        "Green":    195,
        "Grey":     205,
        "Source":   "Drop",
        "RecipeID": 4414,
        "Reagents": {
			"Bronze Tube": 4,
			"Iron Strut": 1,
			"Heavy Blasting Powder": 4,
			"Medium Leather": 4
        }
    },
	"Powerful Seaforium Charge": {
        "ID":       18594,
        "Learn":    275,
        "Yellow":   275,
        "Green":    285,
        "Grey":     295,
        "Source":   "Vendor",
        "Reagents": {
			"Thorium Widget": 2,
			"Dense Blasting Powder": 3,
			"Rugged Leather": 2,
			"Refreshing Spring Water": 1
        }
    },
	"Practice Lock": {
        "ID":       6712,
        "Learn":    100,
        "Yellow":   115,
        "Green":    122,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Bar": 1,
			"Handful of Copper Bolts": 2,
			"Weak Flux": 1
        }
    },
	"Red Firework": {
        "ID":       9318,
        "Learn":    150,
        "Yellow":   150,
        "Green":    162,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Red Rocket Cluster": {
        "ID":       21576,
        "Learn":    225,
        "Yellow":   225,
        "Green":    237,
        "Grey":     250,
        "Source":   "Seasonal",
        "Reagents": {
			"Solid Blasting Powder": 1,
			"Thick Leather": 1
        }
    },
	"Rose Colored Goggles": {
        "ID":       10503,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 6,
			"Star Ruby": 2
        }
    },
	"Rough Blasting Powder": {
        "ID":       4357,
        "Learn":    1,
        "Yellow":   20,
        "Green":    30,
        "Grey":     40,
        "Source":   "Trainer",
        "Reagents": {
			"Rough Stone": 1
        }
    },
	"Rough Boomstick": {
        "ID":       4362,
        "Learn":    50,
        "Yellow":   80,
        "Green":    95,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Tube": 1,
			"Handful of Copper Bolts": 1,
			"Wooden Stock": 1
        }
    },
	"Rough Copper Bomb": {
        "ID":       4360,
        "Learn":    30,
        "Yellow":   60,
        "Green":    75,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Bar": 1,
			"Handful of Copper Bolts": 1,
			"Rough Blasting Powder": 2,
			"Linen Cloth": 1
        }
    },
	"Rough Dynamite": {
        "ID":       4358,
        "Learn":    1,
        "Yellow":   30,
        "Green":    45,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
			"Rough Blasting Powder": 2,
			"Linen Cloth": 1
        }
    },
	"Salt Shaker": {
        "ID":       15846,
        "Learn":    250,
        "Yellow":   270,
        "Green":    280,
        "Grey":     290,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Casing": 1,
			"Thorium Bar": 6,
			"Gold Power Core": 1,
			"Unstable Trigger": 4
        }
    },
	"Shadow Goggles": {
        "ID":       4373,
        "Learn":    120,
        "Yellow":   145,
        "Green":    157,
        "Grey":     170,
        "Source":   "Drop",
        "RecipeID": 4410,
        "Reagents": {
			"Medium Leather": 4,
			"Shadowgem": 2
        }
    },
	"Silver Contact": {
        "ID":       4404,
        "Learn":    90,
        "Yellow":   110,
        "Green":    125,
        "Grey":     140,
        "Source":   "Trainer",
        "Reagents": {
			"Silver Bar": 1
        }
    },
	"Silver-plated Shotgun": {
        "ID":       4379,
        "Learn":    130,
        "Yellow":   155,
        "Green":    167,
        "Grey":     180,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Tube": 2,
			"Whirring Bronze Gizmo": 2,
			"Heavy Stock": 1,
			"Silver Bar": 3
        }
    },
	"Small Blue Rocket": {
        "ID":       21558,
        "Learn":    125,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "Seasonal",
        "Reagents": {
			"Coarse Blasting Powder": 1,
			"Medium Leather": 1
        }
    },
	"Small Bronze Bomb": {
        "ID":       4374,
        "Learn":    120,
        "Yellow":   120,
        "Green":    145,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
			"Coarse Blasting Powder": 4,
			"Bronze Bar": 2,
			"Silver Contact": 1,
			"Wool Cloth": 1
        }
    },
	"Small Green Rocket": {
        "ID":       21559,
        "Learn":    125,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "Seasonal",
        "Reagents": {
			"Coarse Blasting Powder": 1,
			"Medium Leather": 1
        }
    },
	"Small Red Rocket": {
        "ID":       21557,
        "Learn":    125,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "Seasonal",
        "Reagents": {
			"Coarse Blasting Powder": 1,
			"Medium Leather": 1
        }
    },
	"Small Seaforium Charge": {
        "ID":       4367,
        "Learn":    100,
        "Yellow":   130,
        "Green":    145,
        "Grey":     160,
        "Source":   "Drop",
        "RecipeID": 4409,
        "Reagents": {
			"Coarse Blasting Powder": 2,
			"Copper Modulator": 1,
			"Light Leather": 1,
			"Refreshing Spring Water": 1
        }
    },
	"Snake Burst Firework": {
        "ID":       19026,
        "Learn":    250,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Vendor",
        "Reagents": {
			"Dense Blasting Powder": 2,
			"Runecloth": 2,
			"Deeprock Salt": 1
        }
    },
	"Sniper Scope": {
        "ID":       10548,
        "Learn":    240,
        "Yellow":   260,
        "Green":    270,
        "Grey":     280,
        "Source":   "Drop",
        "RecipeID": 10608,
        "Reagents": {
			"Mithril Tube": 1,
			"Star Ruby": 1,
			"Truesilver Bar": 2
        }
    },
	"Snowmaster 9000": {
        "ID":       17716,
        "Learn":    190,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Seasonal",
        "Reagents": {
			"Mithril Bar": 8,
			"Gyrochronatom": 4,
			"Snowball": 4,
			"Frost Oil": 1
        }
    },
	"Solid Blasting Powder": {
        "ID":       10505,
        "Learn":    175,
        "Yellow":   175,
        "Green":    185,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
			"Solid Stone": 2
        }
    },
	"Solid Dynamite": {
        "ID":       10507,
        "Learn":    175,
        "Yellow":   175,
        "Green":    185,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
			"Solid Blasting Powder": 1,
			"Silk Cloth": 1
        }
    },
	"Spellpower Goggles Xtreme": {
        "ID":       10502,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Drop",
        "RecipeID": 10605,
        "Reagents": {
			"Thick Leather": 4,
			"Star Ruby": 2
        }
    },
	"Spellpower Goggles Xtreme Plus": {
        "ID":       15999,
        "Learn":    270,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Drop",
        "RecipeID": 16045,
        "Reagents": {
			"Spellpower Goggles Xtreme": 1,
			"Star Ruby": 4,
			"Enchanted Leather": 2,
			"Runecloth": 8
        }
    },
	"Standard Scope": {
        "ID":       4406,
        "Learn":    120,
        "Yellow":   135,
        "Green":    147,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Tube": 1,
			"Moss Agate": 1
        }
    },
	"Steam Tonk Controller": {
        "ID":       22728,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
			"Thorium Widget": 2,
			"Mithril Casing": 1,
			"Gold Power Core": 1
        }
    },
	"Target Dummy": {
        "ID":       4366,
        "Learn":    85,
        "Yellow":   115,
        "Green":    130,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Modulator": 1,
			"Handful of Copper Bolts": 2,
			"Bronze Bar": 1,
			"Wool Cloth": 1
        }
    },
	"The Big One": {
        "ID":       10586,
        "Learn":    235,
        "Yellow":   235,
        "Green":    255,
        "Grey":     275,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Casing": 1,
			"Goblin Rocket Fuel": 1,
			"Solid Dynamite": 6,
			"Unstable Trigger": 1
        }
    },
	"Thorium Grenade": {
        "ID":       15993,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Vendor",
        "Reagents": {
			"Thorium Widget": 1,
			"Thorium Bar": 3,
			"Dense Blasting Powder": 3,
			"Runecloth": 3
        }
    },
	"Thorium Rifle": {
        "ID":       15995,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Drop",
        "RecipeID": 16043,
        "Reagents": {
			"Mithril Tube": 2,
			"Mithril Casing": 2,
			"Thorium Widget": 2,
			"Thorium Bar": 4,
			"Deadly Scope": 1
        }
    },
	"Thorium Shells": {
        "ID":       15997,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 16051,
        "Reagents": {
			"Thorium Bar": 2,
			"Dense Blasting Powder": 1
        }
    },
	"Thorium Tube": {
        "ID":       16000,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Vendor",
        "Reagents": {
			"Thorium Bar": 6
        }
    },
	"Thorium Widget": {
        "ID":       15994,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Vendor",
        "Reagents": {
			"Thorium Bar": 3,
			"Runecloth": 1
        }
    },
	"Tranquil Mechanical Yeti": {
        "ID":       21277,
        "Learn":    250,
        "Yellow":   320,
        "Green":    330,
        "Grey":     340,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
			"Cured Rugged Hide": 1,
			"Thorium Widget": 4,
			"Globe of Water": 2,
			"Truesilver Transformer": 2,
			"Gold Power Core": 1
        }
    },
	"Truesilver Transformer": {
        "ID":       18631,
        "Learn":    260,
        "Yellow":   270,
        "Green":    275,
        "Grey":     280,
        "Source":   "Vendor",
        "Reagents": {
			"Truesilver Bar": 2,
			"Elemental Earth": 2,
			"Elemental Air": 1
        }
    },
	"Ultrasafe Transporter - Gadgetzan": {
        "ID":       18986,
        "Learn":    260,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Bar": 12,
			"Truesilver Transformer": 2,
			"Core of Earth": 4,
			"Globe of Water": 2,
			"Aquamarine": 4,
			"Inlaid Mithril Cylinder": 1
        }
    },
	"Unstable Trigger": {
        "ID":       10560,
        "Learn":    200,
        "Yellow":   200,
        "Green":    220,
        "Grey":     240,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 1,
			"Mageweave Cloth": 1,
			"Solid Blasting Powder": 1
        }
    },
	"Voice Amplification Modulator": {
        "ID":       16009,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Drop",
        "RecipeID": 16052,
        "Reagents": {
			"Delicate Arcanite Converter": 2,
			"Gold Power Core": 1,
			"Thorium Widget": 1,
			"Large Opal": 1
        }
    },
	"Whirring Bronze Gizmo": {
        "ID":       4375,
        "Learn":    125,
        "Yellow":   125,
        "Green":    150,
        "Grey":     175,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Bar": 2,
			"Wool Cloth": 1
        }
    },
	"World Enlarger": {
        "ID":       18660,
        "Learn":    260,
        "Yellow":   260,
        "Green":    265,
        "Grey":     270,
        "Source":   "Drop",
        "RecipeID": 18661,
        "Reagents": {
			"Mithril Casing": 1,
			"Thorium Widget": 2,
			"Gold Power Core": 1,
			"Unstable Trigger": 1,
			"Citrine": 1
        }
    }
}

import json
with open('engineering.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)