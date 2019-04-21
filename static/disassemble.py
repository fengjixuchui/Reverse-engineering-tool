from capstone import *
from .assembler import *

def get_capstone_mode(architecture, is_64, extra=None):
	lookup_architecture_capstone =	{
			"SPARC":CS_ARCH_SPARC,
			"x86":CS_ARCH_X86,
			"MIPS":CS_ARCH_MIPS,
			"PowerPC":CS_ARCH_PPC,
			"ARM":CS_ARCH_ARM,
			"x86-64":CS_ARCH_X86
	}
	if(is_64):
		return Cs(lookup_architecture_capstone[architecture], CS_MODE_64)
	else:
		return Cs(lookup_architecture_capstone[architecture], CS_MODE_32)
	if(extra):
		#	needed for arm etc
		raise Exception("Not implemented")

def get_all_registers(CsInsn):
#	cs_instruction = CsInsn(mode, )
	registers = []
	index = 1
	while True:
		try:
			registers.append(CsInsn.reg_name(index))
		except Exception:
			break
	return registers

def decompile(input_bytes, start_address, mode, check=True):	
	decompiled = {
		#	address : [instruction , args]
	}
	target_registers_ids = set()
	target_registers_names = []
	mode.detail = True

	for dissably in mode.disasm(input_bytes, start_address):
		registers = []
		(regs_read, regs_write) = dissably.regs_access()

		if len(regs_read) > 0:
			for r in regs_read:
				registers.append(dissably.reg_name(r))
	
		if len(regs_write) > 0:
			for r in regs_write:
				registers.append(dissably.reg_name(r))

		decompiled["0x%x" % (dissably.address)] = [dissably.mnemonic, dissably.op_str, list(set(registers))]


	for register_id in target_registers_ids:
		target_registers_names.append(dissably.reg_name(register_id))

	return decompiled, target_registers_names

