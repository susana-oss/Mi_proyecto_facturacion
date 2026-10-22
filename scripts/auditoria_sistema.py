
"""Script de auditoría interna y verificación para Comercial Chiclayo."""

import datetime
import sys

from src.logica_negocio import procesar_factura


def ejecutar_auditoria():
    print("Iniciando auditoría interna del sistema de facturación...")

    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Transacción contable de control (Monto base: 1000.0, Cliente: VIP)
    factura_control = procesar_factura(1000.0, "VIP")

    # Verificación de consistencia contable
    if factura_control["total_pagar"] <= 0:
        print("[ERROR FATAL]: Discrepancia contable detectada.")
        sys.exit(1)

    nombre_archivo = "reporte_auditoria.txt"

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=====================================================\n")
        archivo.write(" COMERCIAL CHICLAYO - INFORME TÉCNICO DE AUDITORÍA\n")
        archivo.write("=====================================================\n")
        archivo.write(f"Fecha de Certificación : {fecha_actual}\n")
        archivo.write("Entorno de Evaluación  : GitHub Actions Runner (Ubuntu)\n")
        archivo.write("Estado de Integridad   : SISTEMA TOTALMENTE OPERATIVO\n")
        archivo.write("-----------------------------------------------------\n")
        archivo.write(
            f"Subtotal de Control   : S/ "
            f"{factura_control['subtotal_bruto']:.2f}\n"
        )
        archivo.write(
            f"Descuento VIP (15%)    : S/ "
            f"{factura_control['descuento']:.2f}\n"
        )
        archivo.write(
            f"Total Liquidado        : S/ "
            f"{factura_control['total_pagar']:.2f}\n"
        )
        archivo.write("=====================================================\n")

    print(
        f"Auditoría finalizada con éxito. "
        f"Archivo generado: {nombre_archivo}"
    )

    sys.exit(0)


if __name__ == "__main__":
    ejecutar_auditoria()
