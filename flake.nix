{
  description = "Greyboxing assets for 2d games.";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          name = "greybox2d";
          packages = with pkgs; [
            (python3.withPackages (ps: [
              ps.pillow
            ]))
          ];
        };
      }
    );
}
