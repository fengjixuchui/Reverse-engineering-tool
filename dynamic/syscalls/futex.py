
#	from https://elixir.bootlin.com/linux/latest/source/include/uapi/linux/futex.h#L25

FUTEX_BITSET_MATCH_ANY = 0xffffffff

FUTEX_WAIT = 0
FUTEX_WAKE = 1
FUTEX_FD = 2
FUTEX_REQUEUE = 3
FUTEX_CMP_REQUEUE = 4
FUTEX_WAKE_OP = 5
FUTEX_LOCK_PI = 6
FUTEX_UNLOCK_PI = 7
FUTEX_TRYLOCK_PI = 8
FUTEX_WAIT_BITSET = 9
FUTEX_WAKE_BITSET = 10
FUTEX_WAIT_REQUEUE_PI = 11
FUTEX_CMP_REQUEUE_PI = 12

FUTEX_PRIVATE_FLAG = 128
FUTEX_CLOCK_REALTIME = 256
FUTEX_CMD_MASK = ~(FUTEX_PRIVATE_FLAG | FUTEX_CLOCK_REALTIME)

FUTEX_WAIT_PRIVATE = (FUTEX_WAIT | FUTEX_PRIVATE_FLAG)
FUTEX_WAKE_PRIVATE = (FUTEX_WAKE | FUTEX_PRIVATE_FLAG)
FUTEX_REQUEUE_PRIVATE = (FUTEX_REQUEUE | FUTEX_PRIVATE_FLAG)
FUTEX_CMP_REQUEUE_PRIVATE = (FUTEX_CMP_REQUEUE | FUTEX_PRIVATE_FLAG)
FUTEX_WAKE_OP_PRIVATE = (FUTEX_WAKE_OP | FUTEX_PRIVATE_FLAG)
FUTEX_LOCK_PI_PRIVATE = (FUTEX_LOCK_PI | FUTEX_PRIVATE_FLAG)
FUTEX_UNLOCK_PI_PRIVATE = (FUTEX_UNLOCK_PI | FUTEX_PRIVATE_FLAG)
FUTEX_TRYLOCK_PI_PRIVATE = (FUTEX_TRYLOCK_PI | FUTEX_PRIVATE_FLAG)
FUTEX_WAIT_BITSET_PRIVATE = (FUTEX_WAIT_BITSET | FUTEX_PRIVATE_FLAG)
FUTEX_WAKE_BITSET_PRIVATE = (FUTEX_WAKE_BITSET | FUTEX_PRIVATE_FLAG)
FUTEX_WAIT_REQUEUE_PI_PRIVATE = (FUTEX_WAIT_REQUEUE_PI | FUTEX_PRIVATE_FLAG)
FUTEX_CMP_REQUEUE_PI_PRIVATE = (FUTEX_CMP_REQUEUE_PI |  FUTEX_PRIVATE_FLAG)
