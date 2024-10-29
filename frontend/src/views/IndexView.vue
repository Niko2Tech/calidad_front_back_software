<template>
  <div class="flex flex-col min-h-screen bg-green-conaf-50">
    <!-- Header -->
    <NavBar />

    <!-- Main content: Calculator Form -->
    <main class="flex-grow flex justify-center items-center p-4">
      <form @submit.prevent="enviarRegistro" class="bg-white rounded-lg shadow-lg p-8 w-full max-w-md space-y-4">
        <h2 class="text-2xl font-semibold text-center text-green-conaf-800 mb-4">Registro de Huella de Carbono</h2>
        <p :class="resultado?.includes('error') ? 'text-red-500' : 'text-green-conaf-800'">
          {{ resultado }}
        </p>
        <div>
          <label class="block font-semibold mb-1 text-green-conaf-900">Selecciona un Servicio de Streaming</label>
          <select v-model="selectedServicio" class="w-full p-2 border border-green-conaf-300 rounded">
            <option v-for="servicio in servicios" :key="servicio.id" :value="servicio.id">
              {{ servicio.nombre }}
            </option>
          </select>
        </div>

        <div>
          <label class="block font-semibold mb-1 text-green-conaf-900">Horas de Uso</label>
          <input type="number" v-model="horasUso" min="1" class="w-full p-2 border border-green-conaf-300 rounded" />
        </div>

        <div>
          <label class="block font-semibold mb-1 text-green-conaf-900">CO₂ Calculado (kg)</label>
          <p class="p-2 border rounded bg-green-conaf-100 text-green-conaf-700">{{ co2Calculado.toFixed(2) }} kg CO₂</p>
        </div>

        <button type="submit"
          class="w-full p-2 bg-green-conaf-600 text-white rounded font-semibold hover:bg-green-conaf-700">
          Enviar Registro
        </button>
      </form>
    </main>
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import NavBar from '../components/NavBar.vue'
import Footer from '../components/Footer.vue'

const servicios = ref([])
const selectedServicio = ref(null)
const horasUso = ref(1)  // Inicializado en 1 hora por defecto
const co2Calculado = ref(0)
const resultado = ref(null)

const fetchServicios = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/servicios-streaming/')
    if (response.ok) {
      servicios.value = await response.json()
    } else {
      console.error('Error al obtener los servicios de streaming')
    }
  } catch (error) {
    console.error('Error de red:', error)
  }
}

const calcularCo2 = () => {
  if (selectedServicio.value) {
    const servicio = servicios.value.find(s => s.id === selectedServicio.value)
    co2Calculado.value = horasUso.value * servicio.factor_huella_carbono
  }
}

const enviarRegistro = async () => {
  try {
    const response = await fetch('http://localhost:8000/registros-huella-carbono/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        servicio_streaming: selectedServicio.value,
        horas_uso: horasUso.value,
        usuario: 2,
      })
    })
    if (response.ok) {
      resultado.value = 'Registro calculado exitosamente'
      calcularCo2()
    } else {
      resultado.value = 'Error al enviar el registro'
    }
  } catch (error) {
    resultado.value = 'Error de red: ' + error
  }
}


// Calcula el CO2 al cambiar el servicio o las horas de uso
onMounted(fetchServicios)
</script>
