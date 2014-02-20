classdef FigurePlot < hgsetget
  %FIGUREPLOT Convenience class for creating, displaying and saving plots.
  %   Detailed explanation goes here
  
  properties (SetAccess = private, GetAccess = public)
    FigHandle   % Handle to the figure
    FigTitle    % Figure title
    FileEnding  % Format spec. e.g. 'png', 'jpeg' etc.
    Title       % Title for the plot
    XLabel      % X-label for the plot
    YLabel      % Y-label for the plot
    Format      % The format to save the plot in    
    Resolution  % The resolution to be printed
    ResNumber   % Figure resolution as a number
    Size        % Figure size in pixels
    Names       % List of names for the legend
    Colors      % Line colors
    XVec        % The x-vector to be plotted
    YVecs       % List to hold the y-vectors to be plotted
    Axis        % The plot axis'
  end
  
  properties (SetAccess = public, GetAccess = public)
    LineWidth
    FontSize
  end
  
  methods
    
    % Constructor
    function obj = FigurePlot(FigureTitle, XVec)
      obj.FigTitle = FigureTitle;
      obj.FigHandle = figure('name', FigureTitle);
      obj.XVec = XVec;
      obj.YVecs = [];
      obj.Names = [];
      obj.Colors = [];
      obj.SetDefaults();
    end
    
    % Setting default plot settings
    function SetDefaults(obj)
      obj.YLabel = '';
      obj.XLabel = '';
      obj.Title = '';
      obj.Format = '-depsc2';
      obj.FileEnding = '.eps';
      obj.Resolution = '-r100';
      obj.ResNumber = 100;
      obj.Size = [600 400];
      obj.LineWidth = 1.5;
      obj.FontSize = 12;
      obj.Axis = [];
    end
    
    % Adding lines to be plotted
    function AddYVec(obj, YVec, Name, Color)
      set(obj, 'YVecs', YVec);
      set(obj, 'Names', Name);
      set(obj, 'Colors', Color);
    end
    
    % Set-method for YVecs
    function set.YVecs(obj, YVec)
      obj.YVecs = [obj.YVecs;YVec];
    end
    
    % Set-method for axis'
    function SetAxis(obj, XMin, XMax, YMin, YMax)
      obj.Axis = [XMin XMax YMin YMax];
    end
    
    % Set-method for Names
    function set.Names(obj, Name)
      max_len = 10;
      if length(Name) > max_len
        disp('Line name too long. Defaulting to empty string.')
        Name = '';
      end
      spacing_arg = ['%-', num2str(max_len), 's'];
      padded_name = sprintf(spacing_arg, Name);
      obj.Names = [obj.Names;padded_name];
    end
    
    function set.Colors(obj, Color)
      obj.Colors = [obj.Colors; Color];
    end
    
    % Set plot labels
    function PlotLabels(obj, Title, XLabel, YLabel)
      obj.XLabel = XLabel;
      obj.YLabel = YLabel;
      obj.Title  = Title;
    end
    
    % Set file format. Defaults to PNG
    function FileFormat(obj, Format)
      switch Format
        case {'png', 'PNG'}  
          obj.Format = '-dpng';
          obj.FileEnding = '.png';
        case {'eps' , 'EPS'}
          obj.Format = '-depsc2';
          obj.FileEnding = '.eps';
        case {'jpeg', 'JPEG', 'jpg', 'JPEG'}
          obj.Format = '-djpeg';
          obj.FileEnding = '.jpeg';
        otherwise
          obj.Format = '-dpng';
          obj.FileEnding = '.png';
          disp('File format not reconized. Defaulting to PNG.')
      end
    end
    
    % Change resolution
    function SetResolution(obj, DPI)
      switch DPI
        case 100
          obj.Resolution = '-r100';
          obj.ResNumber = 100;
        case 200
          obj.Resolution = '-r200';
          obj.ResNumber = 200;
        case 300
          obj.Resolution = '-r300';
          obj.ResNumber = 300;
        otherwise
          obj.Resolution = '-r100';
          disp('DPI Value not recongized. Defaulting to 100 DPI')
      end
    end
    
    % Set size
    function SetSize(obj, Width, Height)
      obj.Size = [Width Height];
    end    
    
   
    % Saving plot
    function SavePlot(obj)
      close all;
      NumLines = size(obj.YVecs,1);
      % Checing that at least one Y-vector exists
      if length(obj.YVecs) == 0
        disp('You need to specify at least one y-vector before plotting.');
        return
      end
      
      CurFigure = obj.FigHandle;
      
      % Applying settings
      set(0,'defaultlinelinewidth', obj.LineWidth)
      set(0,'DefaultAxesFontName', 'Helvetica');
      set(0,'DefaultAxesFontSize', obj.FontSize);
      set(0,'DefaultTextFontname', 'Helvetica');
      set(0,'DefaultTextFontSize', obj.FontSize);
  
      hold on;
      title(obj.Title); xlabel(obj.XLabel); ylabel(obj.YLabel);
      if length(obj.Axis) > 0
        axis(obj.Axis);
      end
      
      for i = 1:NumLines
        plot(obj.XVec, obj.YVecs(i,:), obj.Colors(i));
      end
      legend(obj.Names(2:NumLines+1,:));
      
      
      FileName = [obj.FigTitle obj.FileEnding];
      set(gcf,'PaperUnits','inches','PaperPosition',[0 0 obj.Size/obj.ResNumber])
      print(obj.FigHandle, obj.Format, FileName, obj.Resolution);
      close(obj.FigHandle);
    end
    
  end
  
end

