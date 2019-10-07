class Game {

    constructor() {
        this.sky_color = 0x000000;
        this.ground_color = 0xffffff;
        this.sun_color = 0xfdb813;
        this.fog_color = 0xdfddd6;
        
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(this.sky_color);
        
        this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 4096);
        this.camera.aspect = window.innerWidth / window.innerHeight;

        this.canvas = document.getElementById("threejs");
        this.renderer = new THREE.WebGLRenderer({canvas: this.canvas});
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.BasicShadowMap;
        this.renderer.shadowMapCullface = THREE.CullFaceBack;
        this.renderer.gammaInput = true;
        this.renderer.gammaOutput = true;
        
        this.scene.fog = new THREE.Fog(this.fog_color, 0, 20000);
        this.renderer.setClearColor(this.scene.fog.color, 1);
        
        //document.body.appendChild(this.renderer.domElement);

        this.setupStats();
        
        window.addEventListener( 'resize', this.onWindowResize.bind(this), false );

        this.keyboard = new KeyboardState();
        this.setupControls();
        
        this.latency = 0;
        this.time = 0.5;

        this.current_time = performance.now();
        this.last_time = this.current_time;
        this.alpha = 0;

        this.loops = 0;
        this.sim_fps = 64;
        this.skip_ticks = 1000 / this.sim_fps;
        this.max_frame_skip = 10;
        this.next_game_tick = performance.now();
    }

    setupStats(){
        this.stats = new Stats();
        this.up_stats = new Stats();
        function setStatPos(stat, left) {
            stat.domElement.style.position = "absolute";
            stat.domElement.style.left = left + "px";
            stat.domElement.style.top = "0px"
        }
        setStatPos(this.stats, 0);
        setStatPos(this.up_stats, 100);

        //this.up_stats.domElement.style.margin = "0px 0px 0px 80px";
        this.stats.showPanel(1);
        this.up_stats.showPanel(0);

        document.body.appendChild(this.stats.domElement);
        document.body.appendChild(this.up_stats.domElement);
    }
    
    setupControls(){
        this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
    }

    onWindowResize(){
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();

        this.renderer.setSize( window.innerWidth, window.innerHeight );
    }
    
    createTerrain(){
        var generateHeight = function( width, height ) {
            /*
            var data = new Uint8Array( width * height ), perlin = new ImprovedNoise(),
            size = width * height, quality = 2, z = Math.random() * 100;
            for ( var j = 0; j < 4; j ++ ) {
                quality *= 4;
                for ( var i = 0; i < size; i ++ ) {
                    var x = i % width, y = ~~ ( i / width );
                    data[ i ] += Math.abs( perlin.noise( x / quality, y / quality, z ) * 0.5 ) * quality + 10;
                }
            }
            */
            
            var map_range = function(x, a, b, c, d){
                return (x - a) * ((d-c)/(b-a)) + c;
            }
            
            var size = width * height, 
                z = Math.random() * 100;
            
            var data = new Uint8Array(size);
            
            var seed = Math.random();
            var noise = new Noise(seed);
            
            var image_data = new Uint8Array(width*height*4);
            
            for (var x=0; x < width; x++){
                for (var y=0; y < height; y++){

                    //var nx = x/quality - 0.5,
                    //    ny = y/quality - 0.5;
                    
                    var v_noise = noise.perlin2(x/250, y/250);
                    var value = map_range(v_noise, -1, 1, 0, 40); // -1, 1 range to 0, 20 range
                    if (x == 0 && y <= 4){
                        console.log(x +", "+y+":"+value);
                    }
                    
                    data[y*width + x] = value;
                    
                    var offset = (x + y * width) * 4;
                    var color = map_range(value, 0, 40, 0, 255); // elevation range to color range
                    image_data[offset + 0] = color;
                    image_data[offset + 1] = color;
                    image_data[offset + 2] = color;
                    image_data[offset + 3] = 0xff;
                }
            }
            
            return {noise: data, image: {data: image_data, width: width, height: height}};
        }        
        
        var noise = generateHeight(1024, 1024);
        var data = noise["noise"];
        var image_data = noise["image"];
        
        this.setupImage(image_data);

        var data_tex = new THREE.DataTexture(image_data["data"], 1024, 1024, THREE.RGBAFormat);
        data_tex.needsUpdate = true;
        data_tex.center.x = 0.5;
        data_tex.center.y = 0.5;
        data_tex.rotation = Math.PI;
        data_tex.repeat.x = -1;
        
        var material = new THREE.MeshBasicMaterial({map: data_tex, wireframe: false}); //Lambert
        material.flatShading = true;
        
        var quality = 16,
            step = 1024 / quality;
        
        var geometry = new THREE.PlaneGeometry(2000, 2000, 15, 15);
        geometry.dynamic = true;
        geometry.rotateX(- Math.PI / 2);
        
        for (var i=0, l=geometry.vertices.length; i < l; i++){
            var x = i % quality,
                y = Math.floor(i / quality);
            geometry.vertices[i].y = data[(x*step)+(y*step)*1024] * 16;
        }
        
        
        //geometry.computeFlatVertexNormals();
        this.terrainMesh = new THREE.Mesh(geometry, material);
        this.terrainMesh.castShadow = true;
        this.scene.add(this.terrainMesh);
    }
    
    setupImage(data){
        this.sceneOrtho = new THREE.Scene();
        this.cameraOrtho = new THREE.OrthographicCamera(0, window.innerWidth, window.innerHeight, 0, -10, 10);
        var image_data = data["data"],
            width = data["width"],
            height = data["height"];
        var sprite_map = new THREE.DataTexture(image_data, width, height, THREE.RGBAFormat);
        sprite_map.needsUpdate = true;
        //sprite_map.magFilter = THREE.NearestFilter;
        //sprite_map.minFilter = THREE.NearestFilter;
        var sprite_mat = new THREE.SpriteMaterial({map: sprite_map, color: 0xffffff});
        var sprite_width = 256,
            sprite_height = 196;
        var sprite_x = window.innerWidth - (sprite_width / 2),
            sprite_y = window.innerHeight - (sprite_height / 2);
        
        sprite_x -= (sprite_width / 4);
        sprite_y -= (sprite_height / 4);
        
        this.sprite = new THREE.Sprite(sprite_mat);
        this.sprite.scale.set(sprite_width, sprite_height, 0);
        this.sprite.position.set(sprite_x, sprite_y, -10);
        this.sceneOrtho.add(this.sprite);
    }

    init() {
        this.light = new THREE.DirectionalLight(0xffffff, 1);
        this.light.position.set(512, 512, 512);
        this.light.lookAt(512, 0, 512);
        
        this.scene.add(this.light);
        
        this.createTerrain();
        
        this.camera.position.x = 1344;
        this.camera.position.y = 896;
        this.camera.position.z = -1344;
        this.camera.lookAt(0, 0, 0);
        
        /*
        this.camera.position.y = 768;
        this.camera.position.z = 512;
        this.camera.lookAt(0, 0, 0);
        */

        this.setup_network("localhost");

        this.current_time = performance.now();
    }
    
    latency_update(ms){
        this.latency = ms;
        this.socket.emit("ping_back", {ping: ms});
    }
    
    setup_network(ip = "localhost", port = "3000"){
        this.socket = io.connect("http://"+ip+":"+port);
        this.socket.on("pong", this.latency_update.bind(this));
    }
    
    handle_input() {
        this.keyboard.update();
    }

    gameTick() {
        //this.controls.update();
    }

    draw() {
        this.renderer.render(this.scene, this.camera);
        this.renderer.autoClear = false;
        this.renderer.render(this.sceneOrtho, this.cameraOrtho);
    }

    run() {
        requestAnimationFrame(this.run.bind(this));
        this.last_time = this.current_time;
        this.current_time = performance.now();
        this.delta = this.current_time - this.last_time;

        this.handle_input();

        this.loops = 0;

        while (this.current_time > this.next_game_tick && this.loops < this.max_frame_skip) {
            this.up_stats.update();
            this.loops++;
            this.gameTick();
            this.next_game_tick += this.skip_ticks;
        }

        this.draw();

        //monitor performance
        this.stats.update();
    }
}

var game = new Game();
game.init();

game.run();