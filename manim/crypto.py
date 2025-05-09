from manim import *
from manim_slides import Slide

TITLE_FONT_SIZE = 48
CONTENT_FONT_SIZE = 32
SOURCE_FONT_SIZE = 24

class PresentationCrypto(Slide):
    skip_reversing = True

    def write_slide_number(self, inital=1, animation=Write, position=ORIGIN):
        self.slide_no = inital
        self.slide_text = Text(str(inital)).shift(position)
        return animation(self.slide_text)

    def update_slide_number(self, animation=Transform):
        self.slide_no += 1
        new_text = Text(str(self.slide_no)).move_to(self.slide_text)
        return animation(self.slide_text, new_text)

    def next_slide_number_animation(self):
        return self.slide_number.animate(run_time=0.5).increment_value(1)

    def introduction(self):
        title = VGroup(
                Text("Chiffrement homomorphique\nappliqué au Machine Learning", t2c={"homomorphique": BLUE, "Machine Learning": YELLOW}, font_size=TITLE_FONT_SIZE),
                Text("Justin Bossard, Tom Mafille").scale(0.5),
        ).arrange(DOWN, buff=1)

        title += (
            SVGMobject("logob.svg", height=0.7)
            .to_corner(DL)
        )

        self.next_slide(notes="""
                        Salut à tous les amis, c'est David Lafarge Pokémon
                        """)
        self.play(FadeIn(title))

    # def homomorphique(self):


    def construct(self):

        # self.camera.background_color = WHITE
        self.wait_time_between_slides = 0.1

        self.slide_number = (
            Integer(number=1, font_size=SOURCE_FONT_SIZE, edge_to_fix=UR)
            .set_color(BLACK)
            .to_corner(DR)
        )
        self.slide_title = Tex("Context", font_size=TITLE_FONT_SIZE).to_corner(UL)
        self.add_to_canvas(
            slide_number=self.slide_number,
            slide_title=self.slide_title,
        )

        self.introduction()
