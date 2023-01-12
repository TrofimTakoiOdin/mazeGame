import pygame
import Cell


current_cell = Cell.grid_cell[0]
current_cell.visited = True
stack = []

while True:
	Cell.screen.fill(pygame.Color('black'))

	for cell in Cell.grid_cell:
		cell.draw()

	next_cell = current_cell.check_neighbours()
	if next_cell:
		next_cell.visited = True
		Cell.remove_walls(current_cell, next_cell)
		current_cell = next_cell
		stack.append(current_cell)
	elif stack:
		current_cell = stack.pop()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			map_cell = [Cell.check_wall(Cell.grid_cell, x, y) for y in range(Cell.rows * 2 - 1) for x in range(Cell.cols * 2 - 1)]
			for y in range(Cell.rows * 2 - 1):
				for x in range(Cell.cols * 2 - 1):
					if map_cell[x + y * (Cell.cols * 2 - 1)]:
						print(" ", end="")
					else:
						print("#", end="")
				print()

	pygame.display.flip()
	Cell.clock.tick(30)