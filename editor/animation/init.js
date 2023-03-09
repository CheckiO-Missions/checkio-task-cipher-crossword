//Don't change it
requirejs(['ext_editor_io2', 'jquery_190', 'raphael_210'],
    function (extIO, $, rr) {
        function CipherCrosswordCanvas() {

            var colorBlue4 = "#294270";
            var colorBlue3 = "#006CA9";
            var colorBlue1 = "#8FC7ED";

            var x0 = 10,
                y0 = 10,
                cellSize = 50;

            var cellN = 5;

            var sizeX = cellSize * 5 + x0 * 2;
            var sizeY = cellSize * 5 + y0 * 2;

            var attrCell = {"stroke": colorBlue4, "fill": colorBlue1, "stroke-width": 2};
            var attrNumber = {"stroke": colorBlue4, "font-size": cellSize / 5, "font-family": 'verdana'};
            var attrLetter = {"stroke": colorBlue4, "font-size": cellSize * 0.5, "font-family": 'verdana'};


            var paper;

            this.createCanvas = function(dom, template, words, answer){
                paper = Raphael(dom, sizeX, sizeY, 0, 0);

                for (var row = 0; row < template.length; row++) {
                    for (var col = 0; col < template[row].length; col++) {
                        var cell = paper.rect(
                            x0 + cellSize * col,
                            sizeY - cellSize * (cellN - row) - y0,
                            cellSize,
                            cellSize
                        ).attr(attrCell);
                        if (template[row][col] === 0){
                            cell.attr("fill", colorBlue3)
                        }
                        else {
                            paper.text(
                                x0 + cellSize * (col + 0.8),
                                sizeY - cellSize * (cellN - row - 0.2) - y0,
                                template[row][col]
                            ).attr(attrNumber);
                            paper.text(
                                x0 + cellSize * (col + 0.5),
                                sizeY - cellSize * (cellN - row - 0.5) - y0,
                                answer[row][col]
                            ).attr(attrLetter)
                        }
                    }
                }
            }
        }
        var io = new extIO({
            animation: function($expl, data){
                var checkioInput = data.in;
                if (!checkioInput) return;
                var rightResult = data.ext.answer;
                var canvas = new CipherCrosswordCanvas();
                canvas.createCanvas($expl[0], checkioInput[0], checkioInput[1], rightResult);
            }
        });
        io.start();
    }
);
