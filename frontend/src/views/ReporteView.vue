<template>
    <div class="flex flex-col min-h-screen bg-green-conaf-50">
        <NavBar />
        <main class="flex flex-col items-center p-4 flex-grow">
            <h2 class="text-2xl font-bold text-center text-green-conaf-700 mb-4">Reportes de Huella de Carbono</h2>

            <!-- Botones de descarga -->
            <div class="flex space-x-4 mb-4">
                <button @click="descargarExcel"
                    class="p-2 bg-green-conaf-600 text-white rounded font-semibold flex items-center hover:bg-green-conaf-700">
                    <i class="fas fa-file-excel mr-2"></i> Descargar Excel
                </button>
                <button @click="descargarPDF"
                    class="p-2 bg-green-conaf-600 text-white rounded font-semibold flex items-center hover:bg-green-conaf-700">
                    <i class="fas fa-file-pdf mr-2"></i> Descargar PDF
                </button>
            </div>

            <!-- Tabla de reportes -->
            <table class="min-w-full bg-white border border-green-conaf-300">
                <thead>
                    <tr class="bg-green-conaf-700 text-white">
                        <th class="py-2 px-4 border">ID</th>
                        <th class="py-2 px-4 border">Servicio</th>
                        <th class="py-2 px-4 border">Fecha</th>
                        <th class="py-2 px-4 border">Horas de Uso</th>
                        <th class="py-2 px-4 border">CO₂ Calculado (kg)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="reporte in reportes" :key="reporte.id" class="text-center border-b">
                        <td class="py-2 px-4">{{ reporte.id }}</td>
                        <td class="py-2 px-4">{{ reporte.nombre_servicio }}</td> <!-- Nuevo campo -->
                        <td class="py-2 px-4">{{ formatFecha(reporte.fecha) }}</td>
                        <td class="py-2 px-4">{{ reporte.horas_uso }}</td>
                        <td class="py-2 px-4">{{ reporte.co2_calculado }}</td>
                    </tr>
                </tbody>
            </table>
        </main>
        <Footer />
    </div>
</template>

<script setup>
import NavBar from '../components/NavBar.vue'
import Footer from '../components/Footer.vue'
import { ref, onMounted } from 'vue'
import jsPDF from 'jspdf'
import autoTable from 'jspdf-autotable'
import * as XLSX from 'xlsx'

// Estado para almacenar los reportes
const reportes = ref([])

// Función para obtener los reportes del usuario con id 2
const fetchReportes = async () => {
    try {
        const response = await fetch('http://localhost:8000/registros-huella-carbono/')
        if (response.ok) {
            const data = await response.json()
            // Filtrar los reportes para el usuario con id 2
            reportes.value = data.filter(reporte => reporte.usuario === 2)
        } else {
            console.error('Error al obtener los reportes')
        }
    } catch (error) {
        console.error('Error de red:', error)
    }
}

// Función para descargar en Excel
const descargarExcel = () => {
    const worksheet = XLSX.utils.json_to_sheet(reportes.value)
    const workbook = XLSX.utils.book_new()
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Reportes')

    // Generar archivo Excel
    XLSX.writeFile(workbook, 'reportes_co2.xlsx')
}

// Función para descargar en PDF
const descargarPDF = () => {
    const doc = new jsPDF()
    doc.text('Reportes de Huella de Carbono', 14, 10)

    // Crear tabla con datos
    autoTable(doc, {
        startY: 20,
        head: [['ID', 'Fecha', 'Horas de Uso', 'CO₂ Calculado (kg)']],
        body: reportes.value.map(reporte => [reporte.id, reporte.fecha, reporte.horas_uso, reporte.co2_calculado])
    })

    // Guardar archivo PDF
    doc.save('reportes_co2.pdf')
}

// Llamar a la función fetchReportes al montar el componente
onMounted(fetchReportes)
const formatFecha = (fecha) => {
    const date = new Date(fecha)
    return date.toLocaleDateString('es-ES', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric'
    })
}
</script>
