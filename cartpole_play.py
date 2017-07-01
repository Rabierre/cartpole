import gym
import termios
import sys
import tty

class _Getch:
	def __call__(self):
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(3)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch
inkey = _Getch()

keys = {
	'\x1b[A': 3,
	'\x1b[B': 2,
	'\x1b[C': 1,
	'\x1b[D': 0
}

# keys = {
# 	'\x03': 3,
# 	'\x02': 2,
# 	'\x01': 1,
# 	'\x00': 0
# }

env = gym.make('CartPole-v0')
env.reset()
env.render()

while True:
	key = inkey()
	print(key)
	action = keys[key]
	s, r, done, _ = env.step(action)
	env.render()
	if done:
		break
