# Illustrations au trait, une par type d'appareil (ajoutées le 6 octobre 2026).
# Dessin 96×96, trait = couleur de la rubrique (currentColor), aplat clair = class "f".

ICONS = {
"robot": '<ellipse class="f" cx="48" cy="60" rx="34" ry="14"/><path d="M14 56c0-8 15-14 34-14s34 6 34 14v6c0 8-15 14-34 14S14 70 14 62z"/><ellipse cx="48" cy="56" rx="34" ry="14"/><circle cx="48" cy="52" r="5"/><path d="M30 72l-6 6M66 72l6 6"/>',
"station": '<rect class="f" x="54" y="16" width="30" height="62" rx="6"/><rect x="54" y="16" width="30" height="62" rx="6"/><path d="M60 30h18M60 38h18"/><path d="M10 70c0-6 10-10 22-10s22 4 22 10v4c0 6-10 10-22 10S10 80 10 74z"/><ellipse cx="32" cy="70" rx="22" ry="10"/>',
"stick": '<path d="M62 10l-18 58"/><rect class="f" x="52" y="30" width="14" height="22" rx="5" transform="rotate(17 59 41)"/><rect x="52" y="30" width="14" height="22" rx="5" transform="rotate(17 59 41)"/><path d="M58 10h10"/><path d="M24 72h38a6 6 0 0 1 0 12H24a6 6 0 0 1 0-12z"/>',
"handvac": '<path class="f" d="M30 34h34a10 10 0 0 1 10 10v10a10 10 0 0 1-10 10H40z"/><path d="M30 34h34a10 10 0 0 1 10 10v10a10 10 0 0 1-10 10H40z"/><path d="M30 34L12 56l6 6 22-6"/><path d="M58 64v12h12V60"/>',
"mop": '<path d="M56 10L42 66"/><path class="f" d="M22 68h40l6 14H16z"/><path d="M22 68h40l6 14H16z"/><path d="M28 50c-4 4-4 8 0 10M78 54c4 3 4 7 0 9"/><path d="M48 18c4-3 8-3 10 0"/>',
"window": '<rect class="f" x="18" y="14" width="60" height="68" rx="4"/><rect x="18" y="14" width="60" height="68" rx="4"/><path d="M48 14v68M18 48h60"/><rect x="28" y="22" width="14" height="14" rx="3"/><path d="M60 60l10 10M64 58l8 8"/>',
"dryer": '<rect class="f" x="18" y="10" width="60" height="76" rx="6"/><rect x="18" y="10" width="60" height="76" rx="6"/><path d="M18 26h60"/><circle cx="48" cy="56" r="18"/><path d="M40 52c4-4 8 4 12 0s6-2 6-2"/><circle cx="28" cy="18" r="2"/><path d="M62 18h8"/>',
"washer": '<rect class="f" x="18" y="10" width="60" height="76" rx="6"/><rect x="18" y="10" width="60" height="76" rx="6"/><path d="M18 26h60"/><circle cx="48" cy="56" r="18"/><path d="M34 60c6 4 22 4 28 0"/><circle cx="28" cy="18" r="2"/><circle cx="36" cy="18" r="2"/>',
"minwash": '<rect class="f" x="24" y="20" width="48" height="64" rx="8"/><rect x="24" y="20" width="48" height="64" rx="8"/><path d="M34 20v-8h28v8"/><circle cx="48" cy="56" r="14"/><path d="M40 58c5 3 11 3 16 0"/>',
"iron": '<path class="f" d="M14 66c0-16 14-28 34-28h24l8 28z"/><path d="M14 66c0-16 14-28 34-28h24l8 28z"/><path d="M40 38c0-10 8-16 22-16h12v16"/><path d="M26 76h4M40 76h4M54 76h4"/>',
"steamer": '<path class="f" d="M34 40h28l-4 24H38z"/><path d="M34 40h28l-4 24H38z"/><path d="M38 64l-6 20M58 64l6 20"/><path d="M40 30c-4-6 4-8 0-14M50 30c-4-6 4-8 0-14M60 30c-4-6 4-8 0-14"/>',
"rack": '<path d="M14 30h68M14 44h68M14 58h68"/><path d="M20 30l-6 50M76 30l6 50"/><path class="f" d="M30 30h14v22l-7 4-7-4z"/><path d="M30 30h14v22l-7 4-7-4z"/><path d="M54 44h16v18H54z"/>',
"dish": '<rect class="f" x="16" y="16" width="64" height="64" rx="6"/><rect x="16" y="16" width="64" height="64" rx="6"/><path d="M16 30h64"/><path d="M28 70V48M40 70V44M52 70V48M64 70V44"/><circle cx="26" cy="23" r="2"/>',
"airfryer": '<path class="f" d="M24 30c0-10 10-16 24-16s24 6 24 16v42a10 10 0 0 1-10 10H34a10 10 0 0 1-10-10z"/><path d="M24 30c0-10 10-16 24-16s24 6 24 16v42a10 10 0 0 1-10 10H34a10 10 0 0 1-10-10z"/><path d="M24 50h48"/><rect x="38" y="58" width="20" height="6" rx="3"/><circle cx="48" cy="34" r="6"/>',
"pot": '<path class="f" d="M18 40h60v26a16 16 0 0 1-16 16H34a16 16 0 0 1-16-16z"/><path d="M18 40h60v26a16 16 0 0 1-16 16H34a16 16 0 0 1-16-16z"/><path d="M14 40h68"/><path d="M34 40c0-8 6-12 14-12s14 4 14 12"/><path d="M48 28v-6"/><path d="M38 20c-3-4 3-6 0-10M58 20c-3-4 3-6 0-10"/>',
"rice": '<path class="f" d="M20 44h56v22a16 16 0 0 1-16 16H36a16 16 0 0 1-16-16z"/><path d="M20 44h56v22a16 16 0 0 1-16 16H36a16 16 0 0 1-16-16z"/><path d="M20 44c0-14 12-22 28-22s28 8 28 22"/><path d="M42 22h12"/><rect x="40" y="58" width="16" height="8" rx="2"/>',
"bread": '<rect class="f" x="16" y="30" width="64" height="50" rx="8"/><rect x="16" y="30" width="64" height="50" rx="8"/><path d="M30 30c0-10 8-14 18-14s18 4 18 14"/><path d="M28 64h20M28 72h12"/><circle cx="64" cy="66" r="6"/>',
"bin": '<path class="f" d="M24 30h48l-5 52H29z"/><path d="M24 30h48l-5 52H29z"/><path d="M20 30c4-12 16-18 28-18s24 6 28 18"/><path d="M40 46v22M56 46v22"/><path d="M66 18l8-6"/>',
"mower": '<path class="f" d="M18 58c0-12 14-20 30-20s30 8 30 20v6H18z"/><path d="M18 58c0-12 14-20 30-20s30 8 30 20v6H18z"/><circle cx="28" cy="70" r="7"/><circle cx="68" cy="70" r="7"/><path d="M40 38v-8h16v8"/><path d="M8 84h80M14 84l4-6M24 84l3-6M74 84l3-6M84 84l2-6"/>',
"pool": '<path d="M8 66c8 6 16 6 24 0s16-6 24 0 16 6 24 0M8 80c8 6 16 6 24 0s16-6 24 0 16 6 24 0"/><path class="f" d="M24 50c0-12 10-20 24-20s24 8 24 20v6H24z"/><path d="M24 50c0-12 10-20 24-20s24 8 24 20v6H24z"/><path d="M48 30V14h14"/>',
"pressure": '<path class="f" d="M14 40h30v20H14z"/><path d="M14 40h30v20H14z"/><path d="M44 46h22l10-4M44 54h22"/><path d="M76 42l10-8M78 46l12-2M76 50l10 6"/><path d="M22 60v14M36 60v14"/>',
"hose": '<rect class="f" x="30" y="18" width="36" height="40" rx="8"/><rect x="30" y="18" width="36" height="40" rx="8"/><circle cx="48" cy="38" r="9"/><path d="M48 33v5l3 3"/><path d="M48 58v10c0 8-14 8-14 16M26 84c-4-4 2-8-2-12"/>',
"leaf": '<path class="f" d="M22 46h32l8 14H22z"/><path d="M22 46h32l8 14H22z"/><path d="M62 52h22"/><path d="M30 46V34h16v12"/><path d="M70 30c6-6 14-4 14-4s0 10-8 14-10-2-6-10z"/><path d="M68 70c4-6 12-6 12-6s-2 10-10 10-6-2-2-4z"/>',
"weed": '<path d="M70 12L46 64"/><path class="f" d="M38 62h16l-4 10H42z"/><path d="M38 62h16l-4 10H42z"/><path d="M40 78c-2 4 0 6 0 6M46 78v6M52 78c2 4 0 6 0 6"/><path d="M18 84c0-10 4-16 8-20M18 84c2-6 8-10 12-10M70 84c0-8-2-12-6-16"/><path d="M64 10h12"/>',
"litter": '<path class="f" d="M16 50h64v20a12 12 0 0 1-12 12H28a12 12 0 0 1-12-12z"/><path d="M16 50h64v20a12 12 0 0 1-12 12H28a12 12 0 0 1-12-12z"/><path d="M16 50c0-20 14-34 32-34s32 14 32 34"/><path d="M30 50a18 18 0 0 1 36 0"/><circle cx="48" cy="66" r="3"/>',
"bowl": '<rect class="f" x="30" y="10" width="36" height="46" rx="8"/><rect x="30" y="10" width="36" height="46" rx="8"/><path d="M38 24h20"/><path d="M14 70h68l-6 12H20z"/><path d="M48 56v8"/><circle cx="40" cy="66" r="2"/><circle cx="50" cy="66" r="2"/><circle cx="58" cy="66" r="2"/>',
"fountain": '<path class="f" d="M16 58h64l-6 22H22z"/><path d="M16 58h64l-6 22H22z"/><path d="M48 58V36"/><path d="M48 36c-10 0-16 8-18 16M48 36c10 0 16 8 18 16"/><path d="M44 22c0-6 4-10 4-10s4 4 4 10a4 4 0 0 1-8 0z"/>',
"catdoor": '<rect class="f" x="22" y="24" width="52" height="52" rx="10"/><rect x="22" y="24" width="52" height="52" rx="10"/><path d="M32 34h32v32H32z"/><path d="M38 52l4-8 4 6 4-6 4 8"/><path d="M12 88h72"/>',
"ball": '<path class="f" d="M14 50h40l-4 32H18z"/><path d="M14 50h40l-4 32H18z"/><ellipse cx="34" cy="50" rx="20" ry="6"/><circle class="f" cx="70" cy="30" r="11"/><circle cx="70" cy="30" r="11"/><path d="M60 26c6 2 14 0 20-4M60 34c6-2 14 0 20 4"/><path d="M42 40c4-6 10-10 16-12"/>',
"brush": '<path class="f" d="M18 30h44v22H18z"/><path d="M18 30h44v22H18z"/><path d="M22 52v10M30 52v10M38 52v10M46 52v10M54 52v10"/><path d="M62 38h18a6 6 0 0 1 0 12H62"/><path d="M24 76c4-2 8-2 12 0s8 2 12 0"/>',
"roller": '<rect class="f" x="18" y="18" width="42" height="26" rx="13"/><rect x="18" y="18" width="42" height="26" rx="13"/><path d="M60 31h10v14l-8 34"/><path d="M26 26h26M26 36h26"/><path d="M22 66c4-2 6 2 10 0s6 2 10 0"/>',
"groom": '<path class="f" d="M14 48h44a10 10 0 0 1 0 20H14z"/><path d="M14 48h44a10 10 0 0 1 0 20H14z"/><path d="M68 58h16"/><path d="M20 68v8M28 68v8M36 68v8M44 68v8"/><path d="M84 58c0-14-10-24-24-28"/>',
"paw": '<path class="f" d="M48 52c-12 0-20 10-20 18 0 6 6 8 12 6s10-2 16 0 12 0 12-6c0-8-8-18-20-18z"/><path d="M48 52c-12 0-20 10-20 18 0 6 6 8 12 6s10-2 16 0 12 0 12-6c0-8-8-18-20-18z"/><ellipse cx="30" cy="42" rx="6" ry="8"/><ellipse cx="42" cy="30" rx="6" ry="8"/><ellipse cx="56" cy="30" rx="6" ry="8"/><ellipse cx="68" cy="42" rx="6" ry="8"/>',
}

SLUG_ICON = {
"robot-aspirateur-laveur": "robot", "robot-aspirateur-pas-cher": "robot", "robot-aspirateur-poils-animaux": "robot",
"robot-aspirateur-petit-appartement": "robot", "robot-aspirateur-station-vidage": "station",
"robot-lave-vitres": "window", "aspirateur-balai-sans-fil": "stick", "aspirateur-laveur-sans-fil": "mop",
"aspirateur-a-main": "handvac", "nettoyeur-vapeur": "mop",
"seche-linge-pompe-a-chaleur": "dryer", "seche-linge-condensation": "dryer", "lave-linge-sechant": "washer",
"mini-lave-linge": "minwash", "defroisseur-vapeur": "steamer", "centrale-vapeur": "iron", "etendoir-chauffant": "rack",
"mini-lave-vaisselle": "dish", "airfryer": "airfryer", "robot-cuiseur": "pot", "multicuiseur": "pot",
"cuiseur-riz": "rice", "machine-a-pain": "bread", "poubelle-automatique": "bin",
"robot-tondeuse": "mower", "robot-tondeuse-sans-fil-perimetrique": "mower", "robot-tondeuse-pas-cher": "mower",
"robot-piscine": "pool", "robot-piscine-sans-fil": "pool", "nettoyeur-haute-pression": "pressure",
"programmateur-arrosage": "hose", "souffleur-feuilles-batterie": "leaf", "desherbeur-electrique": "weed",
"litiere-autonettoyante": "litter", "litiere-autonettoyante-plusieurs-chats": "litter", "litiere-autonettoyante-pas-cher": "litter",
"distributeur-croquettes-automatique": "bowl", "fontaine-eau-chat": "fountain", "chatiere-electronique": "catdoor",
"lanceur-balle-automatique": "ball", "brosse-anti-poils-chat": "brush", "rouleau-anti-poils": "roller",
"aspirateur-toilettage-chat": "groom", "anti-poils-machine-a-laver": "washer",
}


def art(slug, cls="art"):
    body = ICONS.get(SLUG_ICON.get(slug, ""), ICONS["paw"])
    return (f'<svg class="{cls}" viewBox="0 0 96 96" aria-hidden="true" focusable="false" fill="none" '
            f'stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')
