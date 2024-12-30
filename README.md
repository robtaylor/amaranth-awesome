Awesome Amaranth
----------------

A curated list of awesome projects using or building on the [Amaranth project](https://github.com/amaranth-lang/amaranth).

Please submit a PR if you have any suggestions!

Core Amaranth components
========================
 - [amaranth-soc](https://github.com/amaranth-lang/amaranth-soc): Amaranth System-on-a-Chip Framework.
 - [amaranth-stdio](https://github.com/amaranth-lang/amaranth-stdio): Amaranth stream based standard input and output components.
 - [RFCs](https://amaranth-lang.org/rfcs/): Process for Amaranth feature addition.
 - [template-fpga](https://github.com/amaranth-lang/template-fpga): Template repository for getting started with general Amaranth FPGA projects

Active Projects 
===============

<<<<<<< HEAD
 - [Minerva](https://github.com/minerva-cpu/minerva): is a CPU core that implements the [RISC-V](https://riscv.org/specifications/) RV32IMZicsr instruction set built by the maintainer of Amaranth SoC.
 - [Coreblocks](https://kuznia-rdzeni.github.io/coreblocks): is an experimental, modular out-of-order [RISC-V](https://riscv.org/specifications/) core generator implemented in Amaranth.
 - [Glasgow](https://glasgow-embedded.org/): Glasgow Interface Explorer is a tool for exploring digital interfaces
 - [LUNA](https://github.com/greatscottgadgets/luna): is a toolkit for working with USB using FPGA technology, providing gateware and software to enable USB applications.
 - [Lambdalib](https://github.com/lambdaconcept/lambdalib): Lambdalib is a collection of cores, helpers and tools for Amaranth created and maintained by LambdaConcept.
 - [ORBTrace](https://github.com/orbcode/orbtrace): Orbtrace is a lightweight, cost effective, USB2-HS Debug and Trace interface for ARM CORTEX-M processors.
 - [Tiliqua](https://github.com/apfelaudio/tiliqua): Tiliqua is a powerful, open hardware FPGA-based audio multitool for Eurorack.
 - [amaranth-exercises](https://github.com/RobertBaruch/amaranth-exercises): Graded exercises for Amaranth HDL
 - [amaranth-lib-bl0x](https://github.com/bl0x/amaranth-lib-bl0x): A collection of (useful) modules written in Amaranth-HDL.
 - [amaranth-orchard](https://github.com/ChipFlow/amaranth-orchard): Existing open source cores combined with wrappers and glue to enable Amaranth support.
 - [amaranth-stubs](https://github.com/kuznia-rdzeni/amaranth-stubs): Type stubs for Amaranth
 - [hexastorm](https://github.com/hstarmans/hexastorm): Hexastorm is a full toolkit for working with polygon lasers scanners using FPGA technology; and provides hardware, gateware, and software to enable laser scanning applications.
 - [ili9341spi](https://github.com/kivikakk/ili9341spi): Driver for ILI9341 LCD display. Proving ground for [niar](https://github.com/kivikakk/niar).
 - [learn-fpga-amaranth](https://github.com/bl0x/learn-fpga-amaranth): This repository contains code to follow the excellent learn-fpga tutorial by Bruno Levy from blinker to RISC-V using Amaranth HDL
 - [mtkCPU](https://github.com/bieganski/mtkcpu): mtkCPU is a simple, clear, hackable and very inefficient implementation of RiscV ISA in Amaranth HDL.
 - [niar](https://github.com/kivikakk/niar): A small framework for building projects with Amaranth. Provides support for using CXXRTL, optionally with Zig and zxxrtl.
 - [pytest-amaranth-sim](https://github.com/cr1901/pytest-amaranth-sim): Fixture to automate running Amaranth simulations.
 - [sae](https://github.com/kivikakk/sae): RV32I softcore
 - [sentinel](https://github.com/cr1901/sentinel): Sentinel is a small RISC-V CPU (RV32I_Zicsr) written in Amaranth. It implements the Machine Mode privileged spec, and is designed to fit into ~1000 4-input LUTs or less on an FPGA.
 - [smolarith](https://github.com/cr1901/smolarith): Small arithmetic soft-cores for smol FPGAs.
 - [ROOM](https://github.com/Jimx-/ROOM): 10-stage out-of-order RV64IMFDC CPU
 - [amaranth-examples](https://github.com/cyber-murmel/amaranth-examples): Examples for the Amaranth hardware definition language, enabling the simulation and synthesis of digital circuits using Python.
 - [EMBR RV32](https://github.com/eigenform/ember): A computer architecture project focusing on the RV32 instruction set.
 - [hapenny](https://github.com/cbiffle/hapenny): A half-width RISC-V CPU implementation designed to evaluate the Amaranth HDL, operating internally on 16-bit chunks while executing the RV32I instruction set.
 - [Manta](https://github.com/fischermoseley/manta): A configurable and approachable tool for FPGA debugging and rapid prototyping that facilitates communication between FPGAs and host machines.
 - [naps](https://github.com/apertus-open-source-cinema/naps): Building blocks and tools for FPGA design with Python and Amaranth HDL, including prototypes, stream abstractions, various cores, SOC tools, and experimental projects.
 - [Niar](https://github.com/charlottia/niar): A small framework for building projects with Amaranth and supporting CXXRTL, Zig, and zxxrtl.
 - [patina](https://github.com/zignig/patina): A minimal Rust framework for RISC-V FPGA control plane development.
 - [pytest-amaranth-sim](https://github.com/cr1901/pytest-amaranth-sim): A pytest plugin to automate running Amaranth simulations with easy setup and VCD generation.
 - [maia-sdr](https://github.com/maia-sdr/maia-sdr) Maia SDR is an open-source FPGA-based SDR project focusing on the ADALM Pluto. It uses Amaranth-HDL for many DSP Blocks

Companies using Amaranth
========================

 - [ChipFlow](https://chipflow.io) Custom ASIC platform
 - [LambdaConcept](https://lambdaconcept.com/) On-demand software development and hardware programming for a wide range of embedded systems.
 - [Apertus](https://www.apertus.org/axiom) Manufacturer of open hardware professional digital cinema camera.

Inactive Projects
=================
Projects that have seen no updates for >6 months. There have been many changes in Amaranth in that time period.

*Here be dragons, YMMV.*

 - https://github.com/icebreaker-fpga/icebreaker-amaranth-examples
 - https://github.com/GuzTech/misato - Misato is a RISC-V CPU that supports the RV32I instruction set. 
 - https://github.com/kivikakk/sh1107 - SH1107 driver
 - https://github.com/lambdaconcept/amaranth-to-litex Use amaranth-to-litex to simply import Amaranth code into a Litex project.
 - https://github.com/weshu/Amaranth_LFSR - a re-write of Alexforencich's verilog-lfsr, with Amaranth HDL.
   (Note: there is now a RFC to add and LFSR generator to Amaranth core)  https://github.com/amaranth-lang/rfcs/pull/72)
 - https://github.com/sporniket/amaranth-stuff Amaranth stuff by Sporniket is my collection of essential code written using the Amaranth hdl.
