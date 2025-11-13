#import "book/lib/lyceum/lib.typ": APPENDIX, BACK-MATTER, BODY-MATTER, FRONT-MATTER

#let TEXT-SIZE = 18pt

#show: FRONT-MATTER.with(
  // Document metadata
  title: (
    title: "Book Store\nManagement System",
    subtitle: "Best In The Market",
  ),
  authors: (
    (
      given-name: "Ankush",
      name: "Roy",
      affiliation: "Umakanta Academy (English)",
      email: "ankush3411111@gmail.com",
      location: "Chandrapur, Agartala",
    ),
    (
      given-name: "Shibam",
      name: "Roy",
      affiliation: "Umakanta Academy (English)",
      email: "shibamisgay@gmail.com",
      location: "Santipara, Agartala",
    ),
    (
      given-name: "Uday",
      name: "Barman",
      affiliation: "Umakanta Academy (English)",
      email: "uday@gmail.com",
      location: "India",
    ),
    (
      given-name: "Souharda",
      name: "Saha",
      affiliation: "Umakanta Academy (English)",
      email: "souharda@gmail.com",
      location: "India",
    ),
    (
      given-name: "Subrangshu",
      name: "",
      affiliation: "Umakanta Academy (English)",
      email: "subrangshu@gmail.com",
      location: "India",
    ),
    (),
  ),

  publisher: "",
  location: "",

  keywords: ("book store", ""),
  date: datetime(year: 2025, month: 11, day: 13), // auto => datetime.today()

  // Document general format
  page-size: (width: 210mm, height: 297mm),
  page-margin: (inside: 15mm, rest: 15mm),
  page-binding: left,
  page-fill: color.white, // ivory
  text-font: ("EB Garamond", "Libertinus Serif"),
  text-size: TEXT-SIZE,
  lang-name: "en",
)

= Preface

#lorem(50)

// Show rule for the outline
#show outline.entry.where(
  level: 1,
): it => {
  v(12pt, weak: true)
  strong(it)
}

= Contents

#outline(
  title: none,
  target: heading.where(level: 1),
  indent: auto,
)

#show: BODY-MATTER.with(
  TEXT-SIZE,
  "Chapter",
  ship-part-page: false,
)

= Introduction

#lorem(460)

$ e = m c^2 $

= Methodology

#lorem(520)

== Sub-Section

#lorem(520)

= Source Code

// too expensive, comment when doing work
#show raw: set text(font: "JetBrainsMono NF", size: 10pt)
#align(center, text("main.py", font: "JetBrainsMono NF", size: 12pt, fill: blue))
#raw(read("main.py"), lang: "python")


//----------------------------------------------------------------------------//
//                                  APPENDIX                                  //
//----------------------------------------------------------------------------//

#show: APPENDIX.with(TEXT-SIZE, "Appendix", ship-part-page: false)

= Table of Properties

- PNC - Permutation and combination
- CNC - Chennai National Champions
- PNC - Permutation and combination
- CNC - Chennai National Champions
- PNC - Permutation and combination
- CNC - Chennai National Champions
- PNC - Permutation and combination
- CNC - Chennai National Champions


//----------------------------------------------------------------------------//
//                                BACK-MATTER                                 //
//----------------------------------------------------------------------------//


#set page(margin: (top: -20mm))
#show: BACK-MATTER.with(TEXT-SIZE, ship-part-page: false)

#bibliography("book/bibliography.yml", full: true)
