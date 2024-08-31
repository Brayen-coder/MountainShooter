import pygame

print("Setup start")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print("Setup end")
print("Loop start")
while True:
    # Check for all events
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            print("Quitting...")
            pygame.quit()  # Close window
            quit()  # end pygame
