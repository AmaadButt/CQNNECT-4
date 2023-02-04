import pygame
import cmath

# Initialize Pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Statevector Calculator")

# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    # Get input for theta and phi
    theta_input = input("Enter the value for theta (in degrees): ")
    phi_input = input("Enter the value for phi (in degrees): ")

    # Convert input to radians
    theta = float(theta_input) * (3.14 / 180)
    phi = float(phi_input) * (3.14 / 180)

    # Calculate the statevector
    alpha = (1/2**0.5)*(cmath.cos(theta/2)*cmath.exp(phi*1j))
    beta = (1/2**0.5)*(cmath.sin(theta/2)*cmath.exp((phi+cmath.pi)*1j))
    # Convert alpha and beta to percentage
    alpha_perc = (abs(alpha)**2) * 100
    beta_perc = (abs(beta)**2) * 100

    # Display the statevector
    font = pygame.font.Font(None, 30)
    text = font.render("The statevector is: " + str(alpha) + " |0> + " + str(beta) + " |1>", True, (0, 0, 0))
    screen.blit(text, (50, 50))
    text = font.render("The probability of |0> is: " + str(alpha_perc) + "%", True, (0, 0, 0))
    screen.blit(text, (50, 100))
    text = font.render("The probability of |1> is: " + str(beta_perc) + "%", True, (0, 0, 0))
    screen.blit(text, (50, 150))

    # Update the screen
    pygame.display.flip()
