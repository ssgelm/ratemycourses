#!/usr/bin/python
from ratemycourses.model import *

course = Course(dept='FA', num='15B', name='Arts of the Ming Dynasty', description='Examines a broad array of arts from the Ming Dynasty (1368-1644). The first half of the course focuses on activities in and around the Chinese court. The second half concentrates on monuments related to literati and popular cultures. Usually offered every three years.  Ms. Wong')
course.addTag(Tag.byName('CreativeArts'))
course.addTag(Tag.byName('NonWestern'))
course = Course(dept='FA', num='18B', name='History of Art II: From the Renaissance to the Modern Age', description='Open to all students; first-year students and sophomores are encouraged to enroll. A study of the major styles in architecture, painting, and sculpture of the West from the Renaissance to the early twentieth century. Usually offered every year.  Staff')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='24B', name='Twentieth-Century and Contemporary Latin American Art', description='This course is a selective survey of the outstanding figures and movements that have made significant contributions to the history of Latin American art. Special focus will be on Mexican, Argentinean, Brazilian, Venezuelan and Cuban artists. Usually offered every third year.  Staff')
course.addTag(Tag.byName('CreativeArts'))
course.addTag(Tag.byName('NonWestern'))
course = Course(dept='FA', num='42B', name='The Age of Cathedrals', description='Architecture, sculpture, and painting (including stained glass) in Western Europe from the twelfth to the fifteenth century, with particular attention to the great churches of medieval France. Usually offered every second year.  Mr. McClendon')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='71A', name='Modern Art and Modern Culture', description='A thematic study of modernism in twentieth-century painting and sculpture, emphasizing three trends: primitivism, spiritualism, and the redefinition of reality. Individual artists and art movements will be examined in the context of literature, politics, and aesthetic theory. Artists include Picasso, Matisse, Kandinsky, and Duchamp. Usually offered every third year.  Staff')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='76B', name='History of Photography', description='The history of photography from its invention in 1839 to the present, with an emphasis on developments in America. Photography is studied as a documentary and an artistic medium. Topics include Alfred Stieglitz and the photo-secession, Depression-era documentary, Robert Frank and street photography, and postmodern photography. Usually offered every second year.  Staff')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='120A', name='Modern Architecture', description='Survey of nineteenth- and twentieth-century architecture. Usually offered every second year.   Staff')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='154B', name='Art and Trauma: Israeli, Palestinian, Latin American and United States Art', description='A comparative and critical examination of the various ways in which personal traumas (illness, death, loss) and collective traumas (war, the Holocaust, exile) find meaningful expression in the work of modern and contemporary artists from diverse regions. Special one-time offering, spring 2009.  Ms. Ankori')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='171A', name='Impressionism: Avant-Garde Rebellion in Context', description='Focuses on the major artists from the period 1863 - 1886, from the time of Manet and the Salon des Refuses through the eight group exhibitions of Monet, Renoir, Degas, Cezanne, Pissarro, Morisot, and Cassatt and company. The antithesis of impressionism, its academic rivals, the backdrop of the sociopolitical context, the Second Empire, and the Third Republic will be provided, as well as the roots of the movement\'s dissolution. Usually offered every third year.  Ms. Scott')
course.addTag(Tag.byName('CreativeArts'))
course.addTag(Tag.byName('WritingIntensive'))
course = Course(dept='FA', num='182A', name='The Art of China', description='A survey of Chinese art from antiquity to the Ch\'ing dynasty. Usually offered every second year.  Ms. Wong')
course.addTag(Tag.byName('CreativeArts'))
course.addTag(Tag.byName('NonWestern'))
course = Course(dept='FA', num='3B', name='Introduction to Drawing II', description='Beginning-level course. No previous drawing experience necessary. Preference to first-year students and sophomores. May be repeated once for credit if taught by different instructors. Studio fee: $20 per semester. An introduction to the materials and methods of drawing, intended for both studio majors and non-majors. A topics-based course. Each section will offer basic drawing instruction through focus on a particular theme, such as figure drawing, watercolor, or printmaking.  Mr. Downey, Ms. Lichtman, and Mr. Wardwell')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='4B', name='Three-Dimensional Design II', description='Beginning-level course. Preference to first-year students and sophomores. May be repeated once for credit if taught by different instructors. Studio fee: $25 per semester. See FA 4a for course description. Usually offered every semester.  Mr. Baenziger, Ms. Fair, and Staff')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='7B', name='Life Painting', description='Prerequisite: Any studio art course. Studio fee: $25 per semester. A semester-long course dedicated to the practice and study of  the human form. Students work in oil paint from live models for the duration of the course. Students explore historical and contemporary painting issues surrounding art making from the model. Usually offered every spring.  Mr. Downey')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='8A', name='Sculpture in the Age of New Media: Mutational Mayhem', description='Studio fee: $25 per semester. This course may not be repeated for credit by students who have taken FA 117b in previous years. This course explores sculptural practices through new media techniques and materials, with an emphasis on projects inspired by science and technology. The course is organized to introduce the student to the very basics of 3D modeling with Cinema4D, rapid prototyping (3D printing with the Zcorp plaster printer), digital video with Final Cut Pro, basic electronics (soldering, motors, sensors) and some welding. Students will create projects that combine these media to produce performative sculptures and installations that draw from current developments in Alife, AI, biotechnology, and robotics. Usually offered every year.  Ms. Bucher')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='9A', name='Introduction to Digital Photography', description='Prerequisite: One Brandeis studio art course. May be repeated for credit with permission of the instructor. Studio fee: $20. per semester. An introduction to the visual forms and concepts of the photographic image. A range of digital techniques is covered along with aspects of the history of photography. Students must provide their own digital camera. Field trips and image presentations supplement the studio aspect of the course. Usually offered every semester.  Ms. Hechtman')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='10A', name='Context is Everything: Site Sensitive Photography', description='Prerequisite: Two Brandeis studio art course. May be repeated for credit with permission of the instructor. Studio fee: $20. per semester. An intermediate level studio course in digital photography, designed for students with pre-existing interest/experience in photography or other art media. Various materials and methods of image making are employed with a focus on context: environment, relationship with other images/objects, scale, and form. Students must provide their own digital camera. Usually offered every semester.  Ms. Hechtman')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='103B', name='Intermediate Drawing II', description='Recommended for students who have had previous drawing experience. Studio fee: $30 per semester. See FA 103a.  Mr. Gisholt')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='104B', name='Advanced Drawing II', description='Prerequisites: FA 103a and FA 103b or permission of the instructor. Studio fee: $30 per semester.  See FA 104a for course description. A continuation of FA 104a. Course may be repeated for one semester. Usually offered every year.  Mr. Campbell')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='107B', name='Beginning Painting II', description='Prerequisite: FA 107a or permission of the instructor. Studio fee: $40 per semester. FA 107a and FA 107b are two parts of a year-long experience, intended to begin in the fall and continue in the spring. This is a six-hour per week studio class recommended for freshman and sophomore studio art majors or other students desiring an in-depth painting course. Color theory and various methods of oil painting will be introduced while working from landscape, still life, and the figure. Museum trips and slide lectures will augment studio work.  Ms. Lichtman')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='108B', name='Intermediate Painting II', description='Prerequisite: FA 108a or permission of the instructor.  Studio fee: $40 per semester. An intermediate-level painting course emphasizing the plastic and formal means necessary to create work that will become an increasingly personal statement. Usually offered every year.  Mr. Campbell')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='109A', name='Introduction to Printmaking: Lithography', description='Prerequisite: Previous drawing experience. Studio fee: $50 per semester.  Focus on using lithography to create fine art prints. Students start with direct drawing on plates using lithographic crayon and then move on to digitally generated images. Specific assignments are given to explore the visual possibilities of lithography. Usually offered every second year.  Mr. Gisholt')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='110B', name='Senior Studio II', description='Prerequisites: FA 108a and b, FA 112a and b, or permission of the instructor.  Studio fee: $40 per semester. FA 110a and FA 110b are considered two halves of a full-year experience required for studio art majors. Heuristic in nature, this course culminates in a final studio faculty review of the work produced. Review will take the form of an exhibition. Student work can be undertaken in sculpture or painting or a combination of both. Usually offered every year.  Mr. Baenziger and Mr. Wardwell')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='112B', name='Intermediate Sculpture II', description='Prerequisite: FA 112a.  Studio fee: $50 per semester. Exploration of diverse sculptural concepts utilizing various materials and techniques. Emphasis on personal motivation and development. Usually offered every year.  Ms. Fair')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='FA', num='116A', name='Intermediate Printmaking', description='Prerequisite: Previous drawing experience. This course may not be repeated for credit by students who have taken FA 106a as Intermediate Printmaking in previous years. Studio fee: $50 per semester. Seeks to develop a contemporary attitude toward printmaking. Familiarizes the intermediate printmaker with a range of printmaking techniques, such as intaglio, collagraph, relief, and lithography. Traditional and digital techniques are discussed. Intended for students who have taken FA 105a or b, FA 109a or b or postbaccalaureate students in studio art. Usually offered every semester.  Mr. Gisholt')
course.addTag(Tag.byName('CreativeArts'))
course = Course(dept='CLAS', num='134B', name='The Art and Archaeology of Ancient Rome', description='Surveys the art and architecture of the ancient Romans from the eighth century BCE to the end of the empire in Sicily, mainland Italy (with focus on Rome, Ostia, Pompeii, and Herculaneum), and in the Roman provinces. Usually offered every second year.  Ms. Koloski-Ostrow')
course.addTag(Tag.byName('CreativeArts'))
course.addTag(Tag.byName('Humanities'))
course = Course(dept='CLAS', num='145B', name='Topics in Greek and Roman Art and Archaeology', description='Topics vary from year to year and the course may be repeated for credit. Topics include women, gender, and sexuality in Greek and Roman text and art; daily life in ancient Rome; ancient technology; and Athens and the golden age of Greece.  See Schedule of Classes for the current topic and description. Usually offered every second year.   Ms. Koloski-Ostrow')
course.addTag(Tag.byName('CreativeArts'))
course.addTag(Tag.byName('Humanities'))