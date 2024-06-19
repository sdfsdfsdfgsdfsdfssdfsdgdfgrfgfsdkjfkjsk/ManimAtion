from manim import *
self.add_sound("1.wav")
class OpeningManim(Scene):
    def construct(self):
     
        title = Tex(r"This is some Math equation", font_size=48)
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=48)
        VGroup(title, basel).arrange(DOWN, buff=0.5)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait(1)


        transform_title = Tex("How was the transition?", font_size=36)
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(basel[i], shift=DOWN) for i in range(len(basel))], lag_ratio=0.2),
        )
        self.wait(1)

        
        grid = NumberPlane()
        grid_title = Tex(r"\textbf{Pretty Cool I Guess!}", font_size=45)  # Bold text
        grid_title.move_to(transform_title)
        self.add(grid, grid_title)
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait(1)


        self.play(FadeOut(grid_title))
        self.wait(1)
        grid_transform_title = Tex("This is spiral applied to the grid", font_size=36)
        grid_transform_title.to_edge(UP)

        self.play(FadeIn(grid_transform_title))
        self.wait(1)

        grid.prepare_for_nonlinear_transform()

         
        self.play(
            grid.animate.apply_function(
                lambda p: p + np.array([np.sin(p[1]), np.sin(p[0]), 0]),
            ),
            run_time=3,
        )
        self.wait(2)

        # Clear the scene
        self.play(FadeOut(grid_transform_title), FadeOut(grid))
        self.wait(1)

         
        circle = Circle(radius=1.5, color=BLUE)
        square = Square(side_length=2, color=GREEN)
        triangle = Triangle().scale(1.5).set_color(RED)
        star = Star().scale(1.5).set_color(ORANGE)
        
        self.play(Create(circle))
        self.wait(1)
        
        self.play(Transform(circle, square, path_arc=PI/2))
        self.wait(1)
        
        self.play(Transform(circle, triangle, path_arc=PI/2))
        self.wait(1)
        
        self.play(Transform(circle, star, path_arc=PI/2))
        self.wait(1)


        combined_shape = VGroup(circle)
        spiral = ParametricFunction(
            lambda t: np.array([
                t * np.cos(t),
                t * np.sin(t),
                0
            ]), t_range=np.array([0, 8 * PI, 0.1]), color=WHITE
        ).scale(0.5)

        self.play(
            Transform(combined_shape, spiral),
            run_time=3
        )
        self.wait(2)

        
        for _ in range(3):
            self.play(spiral.animate.rotate(2 * PI).set_color(GREEN), run_time=2)
            self.wait(1)

   
        
        self.play(FadeOut(spiral))
        self.wait(1)
        


if __name__ == "__main__":
    from manim import config, tempconfig
    config.media_width = "100%"
    scene = OpeningManim()
    scene.render()
