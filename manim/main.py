from manim import *
from manim_slides import Slide
from manim_slides.slide.animation import Wipe

FONT_TITLE = 38
FONT_CONTENT = 32
TITLE_SCALE = 0.8

Text.set_default(font_size = FONT_TITLE, font = "CMU Serif")
Tex.set_default(font_size = FONT_CONTENT)

class Presentation(Slide):

    skip_reversing = True

    part1 = Text("I - Le chiffrement homomorphe")
    part2 = Text("II - Reconnaissance d'image à partir de données chiffrées")
    part3 = Text("III - Implémentation")

    slide_title = Text("Sommaire").scale(TITLE_SCALE).to_corner(UL)

    def nextSubpart(self, nextSubpart):
        self.play(Write(nextSubpart))
        self.next_slide()
        self.play(FadeOut(nextSubpart))

    def nextPart(self, nextPart):
        self.play(self.slide_title.animate.scale(1 / TITLE_SCALE).move_to(ORIGIN))
        nextPart.move_to(ORIGIN)
        self.play(Transform(self.slide_title, nextPart))

        self.next_slide()

        self.play(self.slide_title.animate.scale(TITLE_SCALE).to_corner(UL))



    def introduction(self):
        title = VGroup(
                Text("Chiffrement homomorphique\nappliqué au Machine Learning", t2c={"homomorphique": BLUE, "Machine Learning": YELLOW}),
                Text("Justin Bossard, Tom Mafille").scale(0.5),
                ).arrange(DOWN, buff = 1)

        title += SVGMobject("logob.svg", height = 0.7).to_corner(DL)

        self.next_slide(notes="""
                        Salut à tous les amis, c'est David Lafarge Pokémon
                        """)
        self.play(FadeIn(title))
        self.next_slide()
        self.wipe(title)


        plan = VGroup(self.part1, self.part2, self.part3,).arrange(DOWN, buff = 0.5)

        self.play(FadeIn(self.slide_title, plan))
        self.next_slide()
        
        self.play(FadeOut(plan))
        self.nextPart(self.part1)


    def chiffrementHomomorphe(self):

        subpart1 = Text("Définition générale")
        subpart2 = Text("Comment ça marche ?")
        subpart3 = Text("Principes à respecter")
        subpart4 = Text("Classes de fonctions homomorphes")
        subpart5 = Text("Exemple d'une fonction homomorphe partielle :\nle chiffrement de Paillier")
        subpart6 = Text("Application du chiffrement de Paillier")


        self.nextSubpart(subpart1)
        
        content1 = Tex(r'Soit $m_{1}$ et $m_{2}$ deux messages clairs, $\bigstar$ une opération simple et $E$ un schéma de chiffrement.\\$E$ est dit homomorphe si on a :$$E(m_{1} \bigstar m_{2}) = E(m_{1}) \bigstar E(m_{2})$$')
        self.play(Write(content1))

        self.next_slide()
        self.play(Unwrite(content1))

        self.nextSubpart(subpart2)

        self.next_slide()

        self.nextSubpart(subpart3)
        self.next_slide()

        self.nextSubpart(subpart4)
        self.next_slide()

        self.nextSubpart(subpart5)
        self.next_slide()

        self.nextSubpart(subpart6)
        self.next_slide()

    def construct(self):
        self.wait_time_between_slides = 0.1

        
        self.introduction()
        self.chiffrementHomomorphe()

        self.nextPart(self.part2)
