import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PrimeTech Solutions | Sistemas e Automações",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_code = """
<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PrimeTech Solutions - Tecnologia e Automação</title>
    <!-- Three.js para o ambiente 3D avançado -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        :root {
            --bg-deep: #07070c;
            --bg-card: #10101a;
            --bg-card-hover: #161624;
            --accent-cyan: #00f2fe;
            --accent-blue: #4facfe;
            --accent-purple: #7f00ff;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
        }

        * { box-sizing: border-box; scroll-behavior: smooth; }

        body {
            background-color: var(--bg-deep);
            color: var(--text-main);
            font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }

        .tech-bg {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: 
                linear-gradient(to bottom, rgba(7,7,12,0.85), rgba(7,7,12,0.98)),
                radial-gradient(circle at 50% 20%, rgba(127,0,255,0.15) 0%, transparent 60%);
            z-index: -1;
        }

        header {
            padding: 1rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(11, 11, 20, 0.85);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255,255,255,0.08);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            color: #fff;
        }
        .logo span { color: var(--accent-cyan); }

        nav {
            display: flex;
            gap: 1.5rem;
            align-items: center;
        }

        nav a {
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            transition: color 0.2s;
        }
        nav a:hover { color: var(--accent-cyan); }

        .btn-header {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            color: var(--bg-deep);
            padding: 0.5rem 1.2rem;
            border-radius: 6px;
            font-weight: 700;
            text-decoration: none;
            font-size: 0.85rem;
        }

        .hero {
            padding: 3rem 5% 1rem 5%;
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
        }

        #canvas-container {
            width: 100%;
            height: 350px;
            margin: 0 auto;
            cursor: grab;
        }
        #canvas-container:active { cursor: grabbing; }

        .hero h1 {
            font-size: 2.8rem;
            font-weight: 900;
            margin-bottom: 1rem;
            color: #fff;
            letter-spacing: -1px;
        }

        .hero h1 span {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            font-size: 1.15rem;
            color: var(--text-muted);
            margin-bottom: 1.5rem;
        }

        .cta-btn {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            color: var(--bg-deep);
            padding: 0.8rem 2rem;
            font-size: 0.95rem;
            font-weight: 800;
            border-radius: 8px;
            text-decoration: none;
            box-shadow: 0 0 25px rgba(0, 242, 254, 0.35);
            display: inline-block;
            transition: transform 0.2s;
        }
        .cta-btn:hover { transform: translateY(-2px); }

        .section {
            padding: 4rem 5%;
            max-width: 1000px;
            margin: 0 auto;
        }

        .section-title {
            font-size: 1.8rem;
            margin-bottom: 2rem;
            text-align: center;
            color: #fff;
            font-weight: 800;
        }

        .flow-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.5rem;
        }
        .flow-card {
            background-color: var(--bg-card);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 12px;
            padding: 1.8rem;
        }
        .flow-card h4 { color: #fff; margin-top: 0; font-size: 1.1rem; margin-bottom: 0.8rem; }
        .flow-card p { color: var(--text-muted); margin: 0; font-size: 0.95rem; }

        .services-stack {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        .service-item {
            background-color: var(--bg-card);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 10px;
            padding: 1.2rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.2s;
        }
        .service-item:hover {
            border-color: var(--accent-cyan);
            background-color: var(--bg-card-hover);
        }
        .service-item h4 { color: #fff; margin: 0; font-size: 1rem; font-weight: 600; }
        .service-item span { color: var(--accent-cyan); font-size: 0.8rem; font-weight: 500; background: rgba(0,242,254,0.05); padding: 0.2rem 0.6rem; border-radius: 4px; }

        .diff-box {
            background: linear-gradient(135deg, rgba(16,16,26,0.95), rgba(22,22,36,0.95));
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 16px;
            padding: 2.5rem;
            text-align: center;
        }
        .diff-steps {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
            margin-top: 1.5rem;
        }
        .diff-step-pill {
            background: rgba(127, 0, 255, 0.15);
            border: 1px solid rgba(127, 0, 255, 0.4);
            color: #fff;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            font-size: 0.9rem;
            font-weight: 600;
        }

        .whatsapp-float {
            position: fixed;
            bottom: 25px;
            right: 25px;
            background: #25d366;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            box-shadow: 0 4px 20px rgba(37, 211, 102, 0.5);
            z-index: 1000;
            text-decoration: none;
            transition: transform 0.3s;
        }
        .whatsapp-float:hover { transform: scale(1.1); }

        footer {
            text-align: center;
            padding: 2.5rem;
            color: var(--text-muted);
            border-top: 1px solid rgba(255,255,255,0.05);
            font-size: 0.85rem;
        }
    </style>
</head>
<body>

    <div class="tech-bg"></div>

    <header>
        <div class="logo">Prime<span>Tech</span></div>
        <nav>
            <a href="#problema">O Problema</a>
            <a href="#solucao">Transformação</a>
            <a href="#servicos">Serviços</a>
            <a href="#diferencial">Diferencial</a>
        </nav>
        <a href="https://wa.me/5511999999999?text=Olá,%20gostaria%20de%20conversar%20sobre%20automações%20para%20minha%20empresa." target="_blank" class="btn-header">Falar com Especialista</a>
    </header>

    <!-- 1️⃣ HERO COM COMPUTADOR/SERVIDOR 3D E PARTÍCULAS -->
    <section class="hero">
        <h1>Sua empresa ainda perde tempo com <span>processos manuais</span>?</h1>
        <p>A PrimeTech Solutions transforma tarefas repetitivas em sistemas e automações inteligentes que geram eficiência real para o seu negócio.</p>
        
        <!-- Elemento 3D Interativo (Servidor + Partículas de Dados) -->
        <div id="canvas-container"></div>

        <div style="margin-top: 1rem;">
            <a href="https://wa.me/5511999999999?text=Olá,%20quero%20conhecer%20as%20soluções%20da%20PrimeTech." target="_blank" class="cta-btn">Conheça nossas soluções</a>
        </div>
    </section>

    <!-- 2️⃣ O PROBLEMA -->
    <section id="problema" class="section">
        <h2 class="section-title">O caos operacional diário</h2>
        <div class="flow-grid">
            <div class="flow-card">
                <h4>📄 Planilhas e Documentos</h4>
                <p>Dados descentralizados, arquivos pesados e informações perdidas entre equipes.</p>
            </div>
            <div class="flow-card">
                <h4>📧 E-mails e WhatsApp</h4>
                <p>Atendimento manual repetitivo, falta de histórico e atrasos nas respostas.</p>
            </div>
            <div class="flow-card">
                <h4>👨‍💼 Trabalho Manual</h4>
                <p>Horários desperdiçados em cadastros e relatórios que poderiam ser automatizados.</p>
            </div>
        </div>
    </section>

    <!-- 3️⃣ A TRANSFORMAÇÃO -->
    <section id="solucao" class="section">
        <h2 class="section-title">Do caos à automação inteligente</h2>
        <div class="diff-box">
            <p style="color: var(--text-muted); margin-bottom: 1rem; font-size: 1.05rem;">Como organizamos e escalamos a sua operação corporativa:</p>
            <div class="diff-steps">
                <span class="diff-step-pill">1. CLIENTES</span>
                <span style="color: var(--accent-cyan); align-self: center;">→</span>
                <span class="diff-step-pill">2. AUTOMATIZAÇÃO</span>
                <span style="color: var(--accent-cyan); align-self: center;">→</span>
                <span class="diff-step-pill">3. DADOS SEGUROS</span>
                <span style="color: var(--accent-cyan); align-self: center;">→</span>
                <span class="diff-step-pill">4. RESULTADOS</span>
            </div>
        </div>
    </section>

    <!-- 4️⃣ SERVIÇOS -->
    <section id="servicos" class="section">
        <h2 class="section-title">O que desenvolvemos para sua empresa</h2>
        <div class="services-stack">
            <div class="service-item">
                <h4>01 — Desenvolvimento de Sistemas</h4>
                <span>Python + Gestão + CRUD</span>
            </div>
            <div class="service-item">
                <h4>02 — Automação de Processos</h4>
                <span>Python + Tarefas Repetitivas</span>
            </div>
            <div class="service-item">
                <h4>03 — Integração de APIs</h4>
                <span>Conectando suas Ferramentas</span>
            </div>
            <div class="service-item">
                <h4>04 — Sistemas de Gestão</h4>
                <span>Controle Operacional Completo</span>
            </div>
            <div class="service-item">
                <h4>05 — Soluções para Empresas</h4>
                <span>Infraestrutura e Otimização</span>
            </div>
            <div class="service-item">
                <h4>06 — Segurança e Proteção de Dados</h4>
                <span>Armazenamento Confiável</span>
            </div>
        </div>
    </section>

    <!-- 5️⃣ SEU DIFERENCIAL -->
    <section id="diferencial" class="section">
        <h2 class="section-title">Nosso Diferencial Tecnológico</h2>
        <div class="diff-box">
            <p style="color: var(--text-muted); margin-bottom: 1rem;">Unimos conhecimento profundo de infraestrutura, arquitetura de sistemas e software para entregar valor ponta a ponta:</p>
            <div class="diff-steps">
                <span class="diff-step-pill">Hardware</span>
                <span>↓</span>
                <span class="diff-step-pill">Sistema</span>
                <span>↓</span>
                <span class="diff-step-pill">Banco de Dados</span>
                <span>↓</span>
                <span class="diff-step-pill">APIs</span>
                <span>↓</span>
                <span class="diff-step-pill">Solução Completa</span>
            </div>
        </div>
    </section>

    <!-- CONTATO / CTA FINAL -->
    <section class="hero" style="padding-top: 1rem;">
        <h2 class="section-title">Pronto para transformar sua empresa?</h2>
        <p>Fale diretamente com nossa equipe e descubra como otimizar seus processos ainda esta semana.</p>
        <a href="https://wa.me/5511999999999?text=Olá,%20quero%20conversar%20sobre%20um%20projeto%20para%20minha%20empresa." target="_blank" class="cta-btn" style="font-size: 1.1rem; padding: 1rem 2.5rem;">💬 Falar no WhatsApp agora</a>
    </section>

    <a href="https://wa.me/5511999999999?text=Olá,%20gostaria%20de%20saber%20mais%20sobre%20as%20soluções%20da%20PrimeTech." target="_blank" class="whatsapp-float" title="Falar no WhatsApp">
        💬
    </a>

    <footer>
        <p>&copy; 2026 PrimeTech Solutions. Todos os direitos reservados.</p>
    </footer>

    <!-- Script 3D Avançado: Servidor/Computador + Partículas de Luz + Reação ao Scroll -->
    <script>
        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(container.clientWidth, container.clientHeight);
        container.appendChild(renderer.domElement);

        // Grupo principal para o Servidor/Computador 3D
        const serverGroup = new THREE.Group();

        // 1. Corpo principal do Servidor (Rack / Torre)
        const chassisGeo = new THREE.BoxGeometry(2, 2.6, 1.2);
        const chassisMat = new THREE.MeshStandardMaterial({
            color: 0x141422,
            roughness: 0.2,
            metalness: 0.9
        });
        const chassis = new THREE.Mesh(chassisGeo, chassisMat);
        serverGroup.add(chassis);

        // 2. Painel frontal com leds de conexões (Ranhuras e Luzes)
        for (let i = -0.9; i <= 0.9; i += 0.45) {
            const slotGeo = new THREE.BoxGeometry(1.7, 0.25, 0.1);
            const slotMat = new THREE.MeshStandardMaterial({
                color: 0x1e1e32,
                roughness: 0.4,
                metalness: 0.5
            });
            const slot = new THREE.Mesh(slotGeo, slotMat);
            slot.position.set(0, i, 0.61);
            serverGroup.add(slot);

            // LED de atividade de dados (Luz azul/ciano)
            const ledGeo = new THREE.BoxGeometry(0.12, 0.08, 0.05);
            const ledMat = new THREE.MeshBasicMaterial({ color: 0x00f2fe });
            const led = new THREE.Mesh(ledGeo, ledMat);
            led.position.set(0.7, i, 0.63);
            serverGroup.add(led);
        }

        // 3. Moldura de borda com wireframe luminoso (Efeito Tecnológico)
        const wireFrameGeo = new THREE.BoxGeometry(2.05, 2.65, 1.25);
        const wireFrameMat = new THREE.MeshBasicMaterial({
            color: 0x00f2fe,
            wireframe: true,
            transparent: true,
            opacity: 0.25
        });
        const wireBox = new THREE.Mesh(wireFrameGeo, wireFrameMat);
        serverGroup.add(wireBox);

        scene.add(serverGroup);

        // 4. Sistema de Partículas de Luz e Dados ao redor
        const particleCount = 120;
        const particleGeo = new THREE.BufferGeometry();
        const particlePositions = new Float32Array(particleCount * 3);

        for (let i = 0; i < particleCount * 3; i += 3) {
            particlePositions[i] = (Math.random() - 0.5) * 8;
            particlePositions[i + 1] = (Math.random() - 0.5) * 8;
            particlePositions[i + 2] = (Math.random() - 0.5) * 8;
        }

        particleGeo.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));
        const particleMat = new THREE.PointsMaterial({
            color: 0x00f2fe,
            size: 0.06,
            transparent: true,
            opacity: 0.8
        });
        const particles = new THREE.Points(particleGeo, particleMat);
        scene.add(particles);

        // Iluminação
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.9);
        scene.add(ambientLight);

        const pointLight = new THREE.PointLight(0x00f2fe, 3, 30);
        pointLight.position.set(4, 4, 4);
        scene.add(pointLight);

        const purpleLight = new THREE.PointLight(0x7f00ff, 2, 30);
        purpleLight.position.set(-4, -4, 4);
        scene.add(purpleLight);

        camera.position.z = 4.8;

        // Controle de Rotação por Mouse / Toque (Arraste)
        let isDragging = false;
        let previousMousePosition = { x: 0, y: 0 };
        let targetRotationX = 0;
        let targetRotationY = 0;

        container.addEventListener('mousedown', (e) => {
            isDragging = true;
            previousMousePosition = { x: e.clientX, y: e.clientY };
        });

        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const deltaX = e.clientX - previousMousePosition.x;
            const deltaY = e.clientY - previousMousePosition.y;
            
            serverGroup.rotation.y += deltaX * 0.01;
            serverGroup.rotation.x += deltaY * 0.01;
            
            previousMousePosition = { x: e.clientX, y: e.clientY };
        });

        window.addEventListener('mouseup', () => { isDragging = false; });

        // Suporte a Toque em Dispositivos Móveis
        container.addEventListener('touchstart', (e) => {
            isDragging = true;
            previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
        });

        window.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            const deltaX = e.touches[0].clientX - previousMousePosition.x;
            const deltaY = e.touches[0].clientY - previousMousePosition.y;
            
            serverGroup.rotation.y += deltaX * 0.01;
            serverGroup.rotation.x += deltaY * 0.01;
            
            previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
        });

        window.addEventListener('touchend', () => { isDragging = false; });

        // Reação ao Scroll da Página (Movimento e Mudança de Posição)
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            // O objeto desloca-se ligeiramente e muda de rotação conforme a página desce
            serverGroup.position.y = -scrollY * 0.0015;
            serverGroup.rotation.z = scrollY * 0.0008;
        });

        // Loop de Animação Principal
        function animate() {
            requestAnimationFrame(animate);
            
            // Se não estiver a arrastar, mantém rotação automática suave
            if (!isDragging) {
                serverGroup.rotation.y += 0.004;
                serverGroup.rotation.x = Math.sin(Date.now() * 0.001) * 0.15;
            }

            // Animação das partículas de dados
            const positions = particleGeo.attributes.position.array;
            for (let i = 1; i < positions.length; i += 3) {
                positions[i] -= 0.008; // Movimento para baixo simulando fluxo de dados
                if (positions[i] < -4) positions[i] = 4;
            }
            particleGeo.attributes.position.needsUpdate = true;
            particles.rotation.y -= 0.001;

            renderer.render(scene, camera);
        }
        animate();

        // Responsividade da tela
        window.addEventListener('resize', () => {
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(container.clientWidth, container.clientHeight);
        });
    </script>
</body>
</html>
"""

components.html(html_code, height=2700, scrolling=True)
